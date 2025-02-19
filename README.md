# Video Analytics System

## Overview
This project is a real-time video analytics system that processes a video stream, detects motion, and optionally applies blurring to detected areas. The system is modular and consists of three components:

1. **Streamer** → Reads frames from a video file and sends them for processing.
2. **Detector** → Detects motion in frames and forwards detection data.
3. **Presenter** → Displays frames with detection boxes and applies blurring if enabled.

## Features
- **Real-time motion detection** based on frame differencing.
- **Blurring of detected motion areas** (optional).
- **Automatic shutdown** when the video ends (optional).
- **Multiprocessing-based architecture** for efficiency.
- **Modular design** allows easy modifications and extensions.

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the System
```bash
python src/runner.py --video ./data/testdata.avi [--enable_blur] [--auto_shutdown]
```

### Arguments
- `--video <video_path>` → Path to the input video file.
- `--enable_blur` → Enables blurring of detected motion areas.
- `--auto_shutdown` → Shuts down the system automatically when the video ends.

### Example Commands
#### **Run without blur and keep running after video ends**
```bash
python src/runner.py --video ./data/testdata.avi
```
#### **Run with motion blurring**
```bash
python src/runner.py --video ./data/testdata.avi --enable_blur
```
#### **Run with motion blurring and auto shutdown**
```bash
python src/runner.py --video ./data/testdata.avi --enable_blur --auto_shutdown
```

## File Structure
```
├── src/
│   ├── runner.py       # Entry point of the system
│   ├── streamer.py     # Streamer module
│   ├── detector.py     # Detector module
│   ├── presenter.py    # Presenter module
│   ├── logger_config.py # Centralized logging configuration
├── data/
│   ├── testdata.avi    # Sample test video
├── requirements.txt    # Dependencies
├── README.md          # Documentation
```
