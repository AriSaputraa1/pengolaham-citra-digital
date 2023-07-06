import cv2

image = cv2.imread('Foto.jpg')
print(image.shape)

# Y awal : titik awal koordinat dari atas = 100
# Y akhir : titik akhir koordinat dari atas = 200
# X awal :titik awal koordinat dari kiri = 300
# X ahir : titik akhir koordinat dari kiri 500

crop = image[100:200, 300:500]

cv2.imshow("full",image)
cv2.imshow('crop',crop)
cv2.waitKey(0)
