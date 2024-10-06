import cv2

img = cv2.imread("hedgehog-thing.png")

t_lower = 50 
t_upper = 100

edge=cv2.Canny(img,t_lower,t_upper)

cv2.imshow("original", img)
cv2.imshow("Canny", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()