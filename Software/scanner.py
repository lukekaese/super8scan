import os
import cv2 
import numpy as np

def readimage(pathtoimage, output_dir):
    img = cv2.imread(pathtoimage, cv2.IMREAD_COLOR)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #showimage("originaImage", img)
    #showimage("Grayimage", imgray)
    #showimage("threshold", thresh)
    
    min_area = 8000   # Mindestfläche
    max_area = 900000 # Maximalfläche
    
    ret, thresh = cv2.threshold(imgray, 120, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    max_arreas = []
    for contour in contours:
        if cv2.contourArea(contour) > max_area:
            max_arreas.append(contour)
    
    mask = np.zeros_like(imgray)
    cv2.drawContours(mask, max_arreas, -1, (255), thickness=cv2.FILLED)
    mask_inverted = cv2.bitwise_not(mask)
    
    #img = cv2.bitwise_and(img, img, mask=mask_inverted) 
       
    cv2.imshow("Result (Outside Contours)", img)
    
    
    cv2.drawContours(img, max_arreas, -1, (255, 0, 0), 2)
    

    ret, thresh = cv2.threshold(imgray, 145, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)       
    filtered_contours = []
    for contour in contours:
        if min_area < cv2.contourArea(contour) < max_area:
            filtered_contours.append(contour)
            
    for i, contour in enumerate(filtered_contours):
        M = cv2.moments(contour)
        if M['m00'] != 0:  
            cx = int(M['m10'] / M['m00'])  
            cy = int(M['m01'] / M['m00']) 

            cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1) 
            
            top_left = (cx - 80, cy - 295) 
            bottom_right = (cx + 900, cy + 255)            
            
            x1, y1 = max(0, top_left[0]), max(0, top_left[1])
            x2, y2 = min(img.shape[1], bottom_right[0]), min(img.shape[0], bottom_right[1])
            
            cropped = img[y1:y2, x1:x2]
            output_path = os.path.join(output_dir, f"cropped_{i}.jpg")
            
            cv2.imshow(f"Cropped Image {i}", cropped)
            cv2.imwrite(output_path, cropped) 
            
            cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)
            
    cv2.drawContours(img, filtered_contours, -1, (255, 0, 0), 3)
    showimage("Contoured Image", img)
    
def showimage(imgname, img):
    cv2.imshow(imgname, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

readimage('./pics/IMG00043.JPG', './pics/cropped')
