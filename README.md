## 🔍 Real-Time Object Detection and Tracking in CARLA using YOLO, ByteTrack & StrongSORT

This project demonstrates a CNN-based robotic vision system built in the [CARLA simulator](https://carla.org/), integrating **YOLO** for object detection with **ByteTrack** and **StrongSORT** for robust multi-object tracking. The system enables mobile robots to perceive dynamic environments in real-time, supporting applications in autonomous navigation and intelligent traffic monitoring.

### 🛠 Simulation Environment: CARLA

- High-fidelity urban simulation with dynamic traffic, pedestrians, and variable weather.
- RGB, Depth, and Semantic Segmentation cameras were attached to the vehicle via Python API.
- Simulated camera footage was used to generate training and inference datasets for deep learning.

### ⚙️ Object Detection: YOLO

- [YOLOv11n](https://docs.ultralytics.com/tasks/detect/#models) was trained using the **BDD100K** dataset and CARLA-generated images.
- Detection classes included: `car`, `bus`, `truck`, `bike`, `person`, `traffic light`, etc.
- Achieved **mAP@0.5 = 0.444**, with high precision for frequent classes like `car` and `bus`.
- Real-time performance suitable for mobile and embedded applications.

### 🎯 Object Tracking: ByteTrack & StrongSORT

**ByteTrack**:
- Tracking-by-detection algorithm using IoU matching + Kalman Filter.
- Incorporates low-confidence detections for better robustness.
- Pros: Fast (~6.3 FPS), low ID switches, lightweight.
- Ideal for resource-constrained systems needing real-time tracking.

**StrongSORT**:
- Enhanced DeepSORT with deep Re-ID features for robust identity matching.
- Combines appearance embeddings with motion cues.
- Pros: High MOTA/MOTP, excellent occlusion handling, better in crowded scenes.
- Trade-off: More computationally intensive (~3.8 FPS).

### 🔄 YOLO + Tracker Workflow

```text
[YOLO Detection] → [Confidence Filtering] → [ByteTrack / StrongSORT Association] → [Track Management] → [Visual Output]

```
### Performance Comparison

| Metric               | YOLO + ByteTrack     | YOLO + StrongSORT     |
|----------------------|----------------------|------------------------|
| Frame Rate (FPS)     | ~6.3 FPS             | ~3.8 FPS               |
| ID Switches          | Low                  | Moderate               |
| Occlusion Handling   | Good                 | Excellent              |
| Tracking Accuracy    | Moderate (MOTA/MOTP) | High (MOTA/MOTP)       |
| Re-Identification    | No                   | Yes                    |
| Computational Cost   | Low                  | High                   |
| Real-Time Friendly   | Yes                  | Partially              |



### 📁 Datasets Used
### Datasets Used

- **BDD100K** – for model training.  
  - BDD100K: Images 100K (2020) Dataset Ninja. Available at: [https://datasetninja.com/bdd100k](https://datasetninja.com/bdd100k)
- **CARLA Camera Output** – for simulation-based evaluation and visualizations.
- **Road Sign Detection** – Dataset Ninja (2020). Available at: [https://datasetninja.com/road-sign-detection](https://datasetninja.com/road-sign-detection)
- **Ultralytics Datasets Overview** – Refer to the Ultralytics YOLO Docs for a comprehensive guide on datasets.  
  - Available at: [https://docs.ultralytics.com/datasets/](https://docs.ultralytics.com/datasets/)

### Video output:
[▶️ YOLO with Bytetrack Video](https://github.com/Iyanuoluwa007/Carla/blob/main/Carla%20Bytetrack.mp4)

[▶️ YOLO with StrongSort Video](https://github.com/Iyanuoluwa007/Carla/blob/main/Carla%20Strongsort.mp4)

[![Demo](https://img.shields.io/badge/Watch-Demo-red)](https://github.com/Iyanuoluwa007/Carla/blob/main/Carla%20Strongsort.mp4)

