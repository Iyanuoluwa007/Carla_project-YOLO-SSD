import sim
import time

print("Starting connection to CoppeliaSim...")
sim.simxFinish(-1)  # Close all previous connections
client_id = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

if client_id != -1:
    print("Connected to CoppeliaSim!")
    # Perform some operation (e.g., start simulation)
    sim.simxStartSimulation(client_id, sim.simx_opmode_blocking)
    time.sleep(2)  # Let the simulation run for 2 seconds
    sim.simxStopSimulation(client_id, sim.simx_opmode_blocking)
    sim.simxFinish(client_id)  # Close connection
else:
    print("Failed to connect to CoppeliaSim.")
