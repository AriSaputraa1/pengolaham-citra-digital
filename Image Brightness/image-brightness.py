import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(image, value):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    v = np.clip(v.astype(np.int32) + value, 0, 255).astype(np.uint8)
    hsv_image = cv2.merge((h, s, v))
    adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return adjusted_image

def main():
    image_path = "Foto Contoh.jpg"  # Foto
    original_image = cv2.imread(image_path)

    brightness_value = -50  # Nilai Kecerahan

    adjusted_image = adjust_brightness(original_image, brightness_value)

    # Gambar Asli
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    # Gambar Hasil
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
    plt.title('Adjusted Image')

    # Tampilkan plot gambar
    plt.show()

if __name__ == '__main__':
    main()