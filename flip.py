import cv2
load =cv2.imread('buya.jpg',1)
flip = cv2.flip(load,0)

cv2.imshow('putar gamabr', flip)

cv2.waitKey(0)
cv2.destroyAllWindows()