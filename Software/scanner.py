import cv2 

def readimage(pathtoimage):
    img = cv2.imread(pathtoimage, cv2.IMREAD_COLOR)
    cv2.imshow("Testimage", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


readimage('./pics/test.jpg')

