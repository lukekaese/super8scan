import cv2
import numpy as np

def process_image(path_to_image):
    # load image
    img = cv2.imread(path_to_image, cv2.IMREAD_GRAYSCALE)

    # Binary threshhold
    _, binary_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # 2. Otsu threshhold
    _, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. adaptive Threshholding mean
    adaptive_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # 4. adaptive threshholding gaussian
    adaptive_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)

    # Ergebnisse anzeigen
    cv2.imshow("Original", img)
    cv2.imshow("Binary Threshold", binary_thresh)
    cv2.imshow("Otsu's Threshold", otsu_thresh)
    cv2.imshow("Adaptive Mean", adaptive_mean)
    cv2.imshow("Adaptive Gaussian", adaptive_gaussian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Bild verarbeiten
process_image('./pics/IMG00043.JPG')