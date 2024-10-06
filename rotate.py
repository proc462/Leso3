import cv2

image =  cv2.imread("hedgehog-thing.png")

rotate_img1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotate_img2 = cv2.rotate(image, cv2.ROTATE_180)
rotate_img3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("original", image)
cv2.imshow("right", rotate_img1)
cv2.imshow("upside down", rotate_img2)
cv2.imshow("left", rotate_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()