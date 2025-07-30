# Face, Eye, Smile & Profile Detection with OpenCV

This project uses OpenCV and Haar Cascade classifiers to detect frontal faces, eyes, smiles, and profile faces in real time using your webcam.

## Fictitious Use Case

**Company:** SeguriTech  
**Description:**  
SeguriTech is a fictitious company focused on smart security in office environments. The developed system allows real-time monitoring of employee access and behavior, detecting faces, smiles, and profiles to improve security and workplace atmosphere.

## Features

- Frontal face detection
- Eye detection within the face
- Smile detection
- Profile face detection
- Real-time visualization with rectangles and labels

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)

## Usage

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/seguritech-face-detection.git
   cd seguritech-face-detection
   ```

2. Install dependencies:

   ```sh
   pip install opencv-python numpy
   ```

3. Run the script:

   ```sh
   python practica.py
   ```

4. A window will open showing the real-time video.
   - Press `q` to exit.

## Code Explanation

- Haar Cascade classifiers for face, eyes, smile, and profile are loaded.
- Video capture from the webcam is started.
- For each frame:
  - The frame is converted to grayscale.
  - Frontal and profile faces are detected.
  - For each face, eyes and smiles are detected.
  - Rectangles and labels are drawn over detected features.
- The system stops when the `q` key is pressed.

## Credits

- Haar Cascade Classifiers: [OpenCV](https://opencv.org/)
- Author: [Carlos Ramirez]
