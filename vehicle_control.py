import carla

def spawn_vehicle(client):
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    vehicle_bp = blueprint_library.filter('dodge')[0]
    
    spawn_point = world.get_map().get_spawn_points()[0]
    vehicle = world.spawn_actor(vehicle_bp, spawn_point)
    
    return vehicle

def drive_forward(vehicle, throttle=0.5, steer=0.0):
    control = carla.VehicleControl(throttle=throttle, steer=steer)
    vehicle.apply_control(control)
