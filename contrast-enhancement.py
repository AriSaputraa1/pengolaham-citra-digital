import cv2
import numpy as np

image = cv2.imread('Foto.jpg')

alpha = 3 #Nilai Contrast

adjusted = cv2.convertScaleAbs(image, alpha=alpha)

cv2.imshow('adjusted', adjusted)
cv2.waitKey()
cv2.destroyAllWindows()