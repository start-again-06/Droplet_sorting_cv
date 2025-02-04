import cv2
import numpy as np

def detect_droplets(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred, 30, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    droplet_sizes = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:  
            droplet_sizes.append(area)

    return droplet_sizes
