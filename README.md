# EyeWitness AI: Multi-Camera Restricted Zone Monitoring System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-red)
![HackZen](https://img.shields.io/badge/HackZen-2026-orange)

AI-powered multi-camera surveillance system that detects restricted-zone intrusions in real time using YOLOv8 and OpenCV and instantly identifies the camera and location requiring immediate attention.

---

# Team – VisionX

**Institution:** Bannari Amman Institute of Technology  
**Department:** Artificial Intelligence and Data Science  
**Hackathon:** HackZen Open Challenge 2026  

| Name | Register Number |
|------|----------------|
| Divya Dharshini S | 7376242AD155 |
| Chitha Sowndarya R | 7376242AD131 |
| Dhivyadharshini G | 7376242AD150 |

---

# Problem Statement

Security personnel cannot continuously monitor multiple CCTV feeds simultaneously, which may result in unauthorized access to restricted areas going unnoticed. Traditional surveillance systems mainly record footage and rely heavily on manual observation, leading to delayed responses and increased operator workload.

Therefore, there is a need for an intelligent computer vision-based surveillance system that can automatically detect intrusions in real time and identify the exact camera and location requiring immediate attention.

---

# Objective

- Detect people in real time using computer vision techniques.
- Monitor different restricted zones for different cameras.
- Generate instant alerts when an intrusion occurs.
- Identify the corresponding camera and location.
- Reduce manual monitoring effort and improve security response time.

---

# Proposed Solution

EyeWitness AI is an AI-powered surveillance system developed using **YOLOv8** and **OpenCV**.

The system simultaneously processes multiple camera feeds and detects human presence in each frame. Predefined restricted zones are assigned to every camera according to security requirements.

When a person enters a restricted area, the system automatically classifies the individual as an intruder and generates a real-time alert.

The alert displays both the camera number and its corresponding location, enabling security personnel to quickly identify and respond to potential threats.

---

# Camera Locations

| Camera | Location |
|--------|----------|
| Camera 1 | Main Entrance |
| Camera 2 | Public Walkway |
| Camera 3 | Restricted Laboratory |
| Camera 4 | Staff Entrance |

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| YOLOv8n | Human Detection Model |
| OpenCV | Video Processing and Visualization |
| NumPy | Numerical Operations |
| PyTorch | Deep Learning Backend |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

---

# Dataset

No custom training dataset was used.

The project uses the pretrained **YOLOv8n model** provided by Ultralytics and four CCTV-style surveillance videos to simulate real-world monitoring environments.

### Input Videos

- Camera 1 – Main Entrance
- Camera 2 – Public Walkway
- Camera 3 – Restricted Laboratory
- Camera 4 – Staff Entrance

---

# Methodology / Architecture

```text
Multiple Camera Feeds
        ↓
Frame Acquisition
        ↓
Frame Preprocessing
        ↓
YOLOv8 Person Detection
        ↓
Restricted Zone Analysis
        ↓
Intrusion Detection
        ↓
Camera & Location Identification
        ↓
Alert Generation
        ↓
Multi-Camera Monitoring Dashboard
```

---

# Working Methodology

1. Four surveillance videos are loaded simultaneously.
2. Frames are extracted from each video.
3. YOLOv8 detects people in every frame.
4. Different restricted zones are defined for each camera.
5. The detected person's position is checked against the restricted zone.
6. Intruders are highlighted using red bounding boxes.
7. Safe individuals are highlighted using green bounding boxes.
8. Camera-specific alerts are generated.
9. All camera feeds are displayed simultaneously.

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/divyadharshini2028/EyeWitness-AI
cd EyeWitness-AI
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the application:

```bash
python app.py
```

Press **Q** to exit the monitoring system.

---

# Input Video Structure

```text
videos/
├── camera1.mp4
├── camera2.mp4
├── camera3.mp4
└── camera4.mp4
```

---

# Results and Outputs

### Key Achievements

✅ Monitored four camera feeds simultaneously.

✅ Detected human presence using YOLOv8.

✅ Applied different restricted-zone rules for different cameras.

✅ Generated real-time intrusion alerts.

✅ Identified the exact camera and location of intrusion.

✅ Detected multiple simultaneous intrusions.

---

# Sample Alert Output

```text
ALERT:
CAM 1 – Main Entrance
CAM 4 – Staff Entrance
```

---

# Screenshots

### Four Camera Monitoring Interface

![Dashboard](screenshots/Screenshort1%20(1).png)

### Intrusion Detection

![Intrusion](screenshots/Screenshort1%20(2).png)

### Multiple Intrusions

![Multiple](screenshots/Screenshort1%20(3).png)

### Location-Based Alert

![Alert](screenshots/Screenshort1%20(4).png)

---

# Advantages

- Reduces continuous manual CCTV monitoring.
- Provides real-time intrusion alerts.
- Supports multiple camera feeds.
- Enables faster security response.
- Lightweight implementation suitable for standard computers.
- Easily scalable for larger surveillance systems.

---

# Future Scope

- Integration with live CCTV cameras.
- Mobile notifications through SMS or Telegram.
- Face recognition for authorized personnel.
- Cloud-based surveillance dashboards.
- Automatic evidence screenshot generation.
- Suspicious behavior and anomaly detection.
- Incident logging and reporting systems.
- User-defined restricted zones.

---

# References

- https://docs.ultralytics.com/
- https://opencv.org/
- https://www.python.org/
- https://pytorch.org/

---

# Conclusion

EyeWitness AI demonstrates the practical application of Computer Vision in intelligent surveillance systems by automatically monitoring multiple camera feeds, detecting restricted-zone intrusions, and generating real-time alerts.

The proposed system reduces dependency on manual surveillance, improves response time, and provides a scalable foundation for future AI-enabled security monitoring solutions.

---

# Repository Link

🔗 https://github.com/divyadharshini2028/EyeWitness-AI