import sys  # ✅ Import sys for proper exit handling
import time
import random
import carla
from carla_setup import client  # Import CARLA client from setup script

# Ensure the CARLA client is initialized
if client is None:
    print("CARLA is not set up properly. Ensure `carla_setup.py` is running.")
    sys.exit()  # ✅ Correct way to exit a script

try:
    # Get the CARLA world
    world = client.get_world()
    bp_lib = world.get_blueprint_library()
    spawn_points = world.get_map().get_spawn_points()

    # Choose a vehicle
    vehicle_bp = bp_lib.find('vehicle.dodge.charger')
    spawn_point = random.choice(spawn_points) if spawn_points else None

    if spawn_point is None:
        print("No available spawn points!")
        sys.exit()

    # Try spawning the vehicle
    vehicle = world.try_spawn_actor(vehicle_bp, spawn_point)

    if vehicle is None:
        print("Vehicle spawn failed. Retrying...")
        time.sleep(1)
        vehicle = world.try_spawn_actor(vehicle_bp, spawn_point)

    if vehicle is None:
        print("Vehicle could not be spawned. Exiting.")
        sys.exit()

    print(f"✅ Vehicle spawned successfully! ID: {vehicle.id}")

    # Attach spectator to the vehicle
    spectator = world.get_spectator()
    transform = carla.Transform(
        vehicle.get_transform().transform(carla.Location(x=-4, z=2.5)),
        vehicle.get_transform().rotation
    )
    spectator.set_transform(transform)

    # Enable autopilot
    traffic_manager = client.get_trafficmanager()
    vehicle.set_autopilot(True, traffic_manager.get_port())

    print("🚗 Vehicle autopilot enabled!")

except Exception as e:
    print(f"❌ Error in vehicle spawn: {e}")
    sys.exit()
