import cv2

load =cv2.imread('abah.webp',1)
Size_x , size_y =load.shape[1]*2 , load.shape[0]*2
new_image= cv2.resize(load,(Size_x, size_y))
cv2.imshow('Foto Asli',load)
cv2.imshow('Foto Baru',new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()