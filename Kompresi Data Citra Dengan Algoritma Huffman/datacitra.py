import heapq
from collections import defaultdict


# Node untuk pohon Huffman
class HuffmanNode:
    def __init__(self, pixel=None, frequency=None):
        self.pixel = pixel
        self.frequency = frequency
        self.left = None
        self.right = None

    # Perbandingan node berdasarkan frekuensinya
    def __lt__(self, other):
        return self.frequency < other.frequency


# Membangun tabel frekuensi dari citra
def build_frequency_table(image):
    frequency_table = defaultdict(int)
    for row in image:
        for pixel in row:
            frequency_table[pixel] += 1
    return frequency_table


# Membangun pohon Huffman
def build_huffman_tree(frequency_table):
    priority_queue = []
    for pixel, frequency in frequency_table.items():
        heapq.heappush(priority_queue, HuffmanNode(pixel, frequency))

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        parent = HuffmanNode(frequency=left_child.frequency + right_child.frequency)
        parent.left = left_child
        parent.right = right_child
        heapq.heappush(priority_queue, parent)

    return priority_queue[0]


# Membangun tabel kode Huffman
def build_huffman_table(huffman_tree, prefix="", huffman_table={}):
    if huffman_tree.pixel is not None:
        huffman_table[huffman_tree.pixel] = prefix
    else:
        build_huffman_table(huffman_tree.left, prefix + "0", huffman_table)
        build_huffman_table(huffman_tree.right, prefix + "1", huffman_table)
    return huffman_table


# Kompresi citra menggunakan kode Huffman
def compress_image(image, huffman_table):
    compressed_data = ""
    for row in image:
        for pixel in row:
            compressed_data += huffman_table[pixel]
    return compressed_data


# Dekompresi citra menggunakan kode Huffman
def decompress_image(compressed_data, huffman_tree, width, height):
    decompressed_image = [[0] * width for _ in range(height)]
    current_node = huffman_tree
    x, y = 0, 0
    for bit in compressed_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.pixel is not None:
            decompressed_image[y][x] = current_node.pixel
            x += 1
            if x >= width:
                x = 0
                y += 1
            current_node = huffman_tree
    return decompressed_image


# Contoh penggunaan

# Matriks citra contoh (8x8)
image_matrix = [
    [0, 0, 0, 0, 0, 1, 2, 3],
    [0, 0, 0, 0, 1, 1, 2, 3],
    [0, 0, 0, 1, 1, 2, 2, 3],
    [0, 0, 0, 1, 1, 2, 3, 3],
    [0, 0, 1, 1, 2, 2, 3, 3],
    [0, 0, 1, 1, 2, 2, 3, 3],
    [0, 0, 1, 2, 2, 2, 3, 3],
    [0, 0, 1, 2, 2, 2, 3, 3],
]

# Lebar dan tinggi citra
width = len(image_matrix[0])
height = len(image_matrix)

# Membangun tabel frekuensi
frequency_table = build_frequency_table(image_matrix)

# Membangun pohon Huffman
huffman_tree = build_huffman_tree(frequency_table)

# Membangun tabel kode Huffman
huffman_table = build_huffman_table(huffman_tree)

# Kompresi citra
compressed_data = compress_image(image_matrix, huffman_table)

# Dekompresi citra
decompressed_image = decompress_image(compressed_data, huffman_tree, width, height)

# Mencetak hasil
print("Original Image:")
for row in image_matrix:
    print(row)

print("\nCompressed Data:", compressed_data)

print("\nDecompressed Image:")
for row in decompressed_image:
    print(row)

#note
#Hasil kompresi di cetak dalam bentuk string
