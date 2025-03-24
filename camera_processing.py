import cv2
import numpy as np
import time

# Create display windows
cv2.namedWindow('All Cameras', cv2.WINDOW_NORMAL)
cv2.resizeWindow('All Cameras', 1920, 1080)

cv2.namedWindow('Duplicate RGB', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Duplicate RGB', 800, 600)  # Keep RGB window smaller

def preprocess_image(img):
    """Ensure all images have 3 channels (convert to RGB if needed)."""
    if img.shape[2] == 4:  # If image has 4 channels (RGBA)
        img = img[:, :, :3]  # Drop the alpha channel
    return img

def add_label(image, label, position=(10, 50), font_scale=0.8, color=(255, 255, 255)):
    """Adds a text label to an image."""
    labeled_image = image.copy()  # Work on a copy to avoid modifying original
    cv2.putText(labeled_image, label, position, cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale, color, 2, cv2.LINE_AA)
    return labeled_image  # Return the labeled image

while True:
    try:
        # Convert all sensor images to 3-channel RGB format
        sensor_data_processed = {key: preprocess_image(img) for key, img in sensor_data.items()}

        # Check if all images are available before displaying
        if any(img.shape[0] == 0 for img in sensor_data_processed.values()):
            print("Waiting for camera feeds...")
            continue

        # Get the RGB image **without** label for the Duplicate RGB window
        rgb_clean = sensor_data_processed['rgb_image'].copy()

        # Create a **labeled** RGB image for the "All Cameras" window
        rgb_labeled = add_label(sensor_data_processed['rgb_image'], "RGB Camera")

        # Concatenate images in a 2-row format for display
        top_row = np.concatenate([
            rgb_labeled,  # **Labeled RGB Image for "All Cameras"**
            add_label(sensor_data_processed['sem_image'], "Semantic Segmentation"),
            add_label(sensor_data_processed['inst_image'], "Instance Segmentation")
        ], axis=1)
        
        lower_row = np.concatenate([
            add_label(sensor_data_processed['depth_image'], "Depth Camera"),
            add_label(sensor_data_processed['dvs_image'], "DVS Camera"),
            add_label(sensor_data_processed['opt_image'], "Optical Flow")
        ], axis=1)

        # Combine both rows into a single tiled view
        tiled = np.concatenate((top_row, lower_row), axis=0)

        # Display the combined camera feeds in the main window
        cv2.imshow('All Cameras', tiled)

        # Display the **clean RGB image** in the Duplicate RGB window
        cv2.imshow("Duplicate RGB", rgb_clean)

        # Exit on pressing 'q'
        if cv2.waitKey(1) == ord('q'):
            break
    except Exception as e:
        print(f"Error displaying images: {e}")

# Cleanup: Close all OpenCV windows
cv2.destroyAllWindows()
