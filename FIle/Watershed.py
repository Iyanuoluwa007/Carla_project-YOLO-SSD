import cv2 
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

road = cv2.imread('Computer-Vision-with-Python/DATA/road_image.jpg')
road_copy = np.copy(road)
# road.shape[:2]

marker_image = np.zeros(road.shape[:2],dtype=np.int32)
segments = np.zeros(road.shape,dtype=np.uint8)

# marker_image.shape
# segments.shape

from matplotlib import cm

cm.tab10(0)

def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)

colors = []
for i in range(10):
    colors.append(create_rgb(i))

# Global variables
# Color Choice
n_markers = 10 # 0 - 9
current_marker = 1
# Markers updated by Watershed
marks_updated = False

# Callback Function
def mouse_callback(event,x,y,flags,param):
    global marks_updated

    if event == cv2.EVENT_FLAG_LBUTTON:
        # Markers passed to the Watershed Algo
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)

        # User Sees
        cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)

    marks_updated = True

# While True
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    cv2.imshow('Watershed Segments',segments)
    cv2.imshow('Road Image', road_copy)

    # Close All Window
    k = cv2.waitKey(1)
    if k == 27: # Esc key
        break

    # Clearing all the color 
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2],dtype=np.int32)
        segments = np.zeros(road.shape,dtype=np.uint8)
        
    # Update Color Choice
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    # Update the Markings
    if marks_updated:

        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)

        segments = np.zeros(road.shape,dtype=np.uint8)

        for color_ind in range(n_markers):
            # Coloring Segmentd, Numpy Call
            segments[marker_image_copy==(color_ind)] = colors[color_ind]



cv2.destroyAllWindows()
