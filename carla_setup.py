import carla
import time

def setup_carla():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        print("✅ Connected to CARLA server!")

        while True:
            time.sleep(1)  # Keep script running in the background

    except Exception as e:
        print(f"❌ Error connecting to CARLA: {e}")

if __name__ == "__main__":
    setup_carla()
