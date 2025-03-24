import sim  # Import the remote API library
import time

# Connect to CoppeliaSim
print("Connecting to CoppeliaSim...")
sim.simxFinish(-1)  # Close any previous connections
client_id = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to port 19999

if client_id != -1:
    print("Connected to CoppeliaSim!")
else:
    print("Failed to connect to CoppeliaSim.")
    exit()

# Example: Get object handle
_, cam_handle = sim.simxGetObjectHandle(client_id, 'Vision_sensor', sim.simx_opmode_blocking)

# Example: Read image from CoppeliaSim's camera
_, resolution, image = sim.simxGetVisionSensorImage(client_id, cam_handle, 0, sim.simx_opmode_streaming)
time.sleep(1)  # Wait for the image stream to initialize

while sim.simxGetConnectionId(client_id) != -1:
    _, resolution, image = sim.simxGetVisionSensorImage(client_id, cam_handle, 0, sim.simx_opmode_buffer)
    if _ == sim.simx_return_ok:
        # Process image (convert to OpenCV format)
        import numpy as np
        import cv2

        img = np.array(image, dtype=np.uint8)
        img = img.reshape(resolution[1], resolution[0], 3)  # HxWxC
        img = cv2.flip(img, 0)  # Flip vertically
        cv2.imshow('CoppeliaSim Camera', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Close connection
sim.simxFinish(client_id)
print("Connection closed.")
