import carla
import time
import random

#  """Continuously control random traffic lights with dynamic duration settings."""

def control_traffic_lights(world):
    # Get all traffic lights in the world
    traffic_lights = [actor for actor in world.get_actors() if isinstance(actor, carla.TrafficLight)]

    if traffic_lights:
        while True:  # Loop to continuously change random traffic lights
            # Select a random traffic light
            traffic_light = random.choice(traffic_lights)
            print(f"\nRandom Traffic Light Selected: ID {traffic_light.id} at {traffic_light.get_location()}")

            # Generate random durations for each light state
            red_time = random.randint(3, 10)    # Random red light duration (3-10 sec)
            yellow_time = random.randint(2, 5)  # Random yellow light duration (2-5 sec)
            green_time = random.randint(5, 12)  # Random green light duration (5-12 sec)

            # Set to red
            traffic_light.set_state(carla.TrafficLightState.Red)
            print(f"Traffic light set to RED for {red_time} seconds")
            time.sleep(red_time)

            # Set to yellow
            traffic_light.set_state(carla.TrafficLightState.Yellow)
            print(f"Traffic light set to YELLOW for {yellow_time} seconds")
            time.sleep(yellow_time)

            # Set to green
            traffic_light.set_state(carla.TrafficLightState.Green)
            print(f"Traffic light set to GREEN for {green_time} seconds")
            time.sleep(green_time)
    else:
        print("No traffic lights found in the environment.")
