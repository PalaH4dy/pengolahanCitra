import cv2

load = cv2.imread('abah.webp',1)

width, hight = load.shape[1], load.shape[0]

rotation = cv2.getRotationMatrix2D((width/2, hight/2),90,1)
img_rotasi = cv2.warpAffine(load,rotation,(width,hight))
cv2.imshow('Image Rotate',img_rotasi)

cv2.waitKey(0)
cv2.destroyAllWindows()