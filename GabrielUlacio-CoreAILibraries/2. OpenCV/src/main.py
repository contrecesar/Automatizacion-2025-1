import cv2
import os
from detectors import detect_faces

INPUT_PATH = 'data/input/sample.jpg'
OUTPUT_PATH = 'data/output/sample_processed.jpg'

# Read image
image = cv2.imread(INPUT_PATH)

# Check if image was loaded
if image is None:
    raise FileNotFoundError(f"Could not load the image from {INPUT_PATH}")

# Apply face detection
image = detect_faces(image)

# Save result
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
cv2.imwrite(OUTPUT_PATH, image)
print(f"Result saved in {OUTPUT_PATH}")
