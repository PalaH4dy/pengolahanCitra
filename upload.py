import cv2

load =cv2.imread('buya.jpg',4)
cv2.imshow('load Image',load)

cv2.waitKey(0)
cv2.destroyAllWindows()