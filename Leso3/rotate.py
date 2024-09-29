import cv2

image =  cv2.imread("nugget.png")

rotate_img1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotate_img2 = cv2.rotate(image, cv2.ROTATE_180)
rotate_img3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", image)
cv2.imshow("90clockwise", rotate_img1)
cv2.imshow("180", rotate_img2)
cv2.imshow("90counterclockwise", rotate_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()