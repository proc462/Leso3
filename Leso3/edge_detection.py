import cv2

img = cv2.imread("nugget.png")

t_lower = 50 #Lower Threshold
t_upper = 250 #Upper Threshold

#Applying the Canny Edge filter
edge=cv2.Canny(img,t_lower,t_upper)

cv2.imshow("original", img)
cv2.imshow("Canny", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()