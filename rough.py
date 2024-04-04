import cv2
import numpy as np

# Read the image
image = cv2.imread('sudoku1.jpg')

# Display original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)
cv2.waitKey(0)

# Apply Gaussian blurring
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 50, 150)
cv2.imshow('Edges', edges)
cv2.waitKey(0)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours by area and shape
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]

# Approximate polygons
polygons = [cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True) for cnt in filtered_contours]

# Filter rectangular shapes
rectangles = [poly for poly in polygons if len(poly) == 4]

# Draw the detected rectangles on the original image
result_image = image.copy()
for rect in rectangles:
    cv2.drawContours(result_image, [rect], -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('Detected Sudoku Board', result_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
