# 🔍 Face Detector | OpenCV Annotation Tool

**Automatically detect human faces in images using Haar Cascades and annotate them with bounding boxes**

[![OpenCV](https://img.shields.io/badge/OpenCV-5.0-blue?logo=opencv)](https://opencv.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-green?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🖼️ Example

| Original Image | Detected Faces |
|----------------|----------------|
| ![Input](data/input/sample.jpg) | ![Output](data/output/sample_processed.jpg) |

---

## ✨ Features
- 🧠 Face detection using Haar Cascade Classifier
- 📦 Simple, clean annotations
- 🗂️ Processes local images from folder
- 💾 Output stored with bounding boxes

---

## 🛠️ Installation
```bash
git clone https://github.com/your-username/face-detector.git
cd face-detector
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Quick Start
1. Add images to data/input/
2. Run detection:
```bash
python src/main.py
```
3. Find annotated images in data/output/
