import cv2

image = cv2.imread("nugget.png")
cv2.imshow("nugget", image)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()