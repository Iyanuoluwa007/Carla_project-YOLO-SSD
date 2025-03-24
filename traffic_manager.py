import carla

def disable_traffic_manager(client):
    """Disable NPCs and traffic manager to remove unwanted vehicles and pedestrians."""
    world = client.get_world()
    traffic_manager = client.get_trafficmanager()
    
    # Disable NPCs by removing all existing vehicles and pedestrians
    all_actors = world.get_actors()
    for actor in all_actors:
        if isinstance(actor, carla.Vehicle) or isinstance(actor, carla.Walker):
            actor.destroy()
    
    # Disable traffic manager control
    traffic_manager.set_global_distance_to_leading_vehicle(100.0)
    traffic_manager.global_percentage_speed_difference(100)
    
    print("Traffic Manager disabled and NPCs removed.")
