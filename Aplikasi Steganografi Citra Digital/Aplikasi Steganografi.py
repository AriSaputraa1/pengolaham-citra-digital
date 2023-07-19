# Impor pustaka yang diperlukan
import cv2
import numpy as np

# Fungsi untuk mengubah data menjadi bit
def string_to_bits(message):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    return binary_message

# Fungsi untuk menyembunyikan bit-data ke dalam gambar
def hide_data(image, data):
    data_size = len(data)

    # Ukuran gambar (lebar x tinggi)
    image_height, image_width, _ = image.shape
    image_size = image_height * image_width

    if data_size > image_size:
        raise ValueError("Ukuran data terlalu besar untuk gambar ini.")

    data_index = 0

    for row in range(image_height):
        for col in range(image_width):
            pixel = image[row, col]

            for color_channel in range(3):  # 3 untuk citra berwarna (RGB)
                if data_index < data_size:
                    # Ambil bit dari data
                    data_bit = int(data[data_index])

                    # Ganti bit LSB dengan bit-data
                    pixel[color_channel] = (pixel[color_channel] & 254) | data_bit
                    data_index += 1
                else:
                    break

    return image

# Fungsi untuk mengekstrak data dari gambar hasil
def extract_data(image, data_size):
    extracted_data = ""
    data_index = 0

    image_height, image_width, _ = image.shape

    for row in range(image_height):
        for col in range(image_width):
            pixel = image[row, col]

            for color_channel in range(3):  # 3 untuk citra berwarna (RGB)
                # Ambil bit-data dari bit LSB
                extracted_data += str(pixel[color_channel] & 1)
                data_index += 1

                if data_index == data_size:
                    return extracted_data

# Contoh Penggunaan
if __name__ == "__main__":
    # Baca gambar
    image_path = "gambar_input.jpg"
    image = cv2.imread(image_path)

    # Data yang akan disembunyikan
    data_to_hide = "Ini adalah pesan rahasia! Ari Ganteng"

    # Ubah data menjadi bit
    hidden_data = string_to_bits(data_to_hide)

    # Sembunyikan data ke dalam gambar
    image_with_hidden_data = hide_data(image.copy(), hidden_data)

    # Simpan gambar hasil
    output_image_path = "gambar_output.jpg"
    cv2.imwrite(output_image_path, image_with_hidden_data)

    # Ekstraksi data dari gambar hasil
    extracted_data = extract_data(image_with_hidden_data, len(hidden_data))
    print("Data tersembunyi yang diekstrak:", extracted_data)