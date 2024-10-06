import cv2

image = cv2.imread("hedgehog-thing.png")
cv2.imshow('Original', image)

Gaussian = cv2.GaussianBlur(image, (7,7),0)
cv2.imshow('Gaussian BLurring', Gaussian)

median = cv2.medianBlur(image, 5 )
cv2.imshow('Median Blurring', median)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()