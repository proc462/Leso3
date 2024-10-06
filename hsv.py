import cv2

image = cv2.imread("hedgehog-thing.png")

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("original", image)
cv2.imshow("hsv format", hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
