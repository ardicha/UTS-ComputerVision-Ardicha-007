import cv2
import numpy as np
import os

# 1. Membuat kanvas putih 
canvas = np.full((400, 400, 3), 255, dtype=np.uint8)

# 2. Gambar karakter: Rumah sederhana
# Dinding rumah (biru muda)
cv2.rectangle(canvas, (120, 180), (280, 320), (173, 216, 230), -1)  # biru muda

# Atap rumah (merah bata)
pts = np.array([[100, 180], [200, 100], [300, 180]], np.int32)
cv2.fillPoly(canvas, [pts], (0, 0, 128))  # merah bata

# Pintu (coklat)
cv2.rectangle(canvas, (180, 240), (220, 320), (42, 42, 165), -1)  # coklat (BGR)

# Jendela kiri
cv2.rectangle(canvas, (130, 210), (160, 240), (255, 255, 255), -1)
cv2.line(canvas, (145, 210), (145, 240), (0, 0, 0), 2)
cv2.line(canvas, (130, 225), (160, 225), (0, 0, 0), 2)

# Jendela kanan
cv2.rectangle(canvas, (240, 210), (270, 240), (255, 255, 255), -1)
cv2.line(canvas, (255, 210), (255, 240), (0, 0, 0), 2)
cv2.line(canvas, (240, 225), (270, 225), (0, 0, 0), 2)

# Label teks
cv2.putText(canvas, "rumah", (145, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

# Simpan karakter awal
cv2.imwrite("output/karakter.png", canvas)

# 3. Transformasi
# a. Translasi (geser posisi)
M_translate = np.float32([[1, 0, 50], [0, 1, 30]]) 
translated = cv2.warpAffine(canvas, M_translate, (400, 400))
cv2.imshow("translasi", translated)
cv2.waitKey()


# b. Rotasi (putar 30 derajat)
center = (200, 200)
M_rotate = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated = cv2.warpAffine(canvas, M_rotate, (400, 400))
cv2.imwrite("output/rotate.png", rotated)

# c. Resize (ubah ukuran jadi 150%)
resized = cv2.resize(canvas, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resize", resized)
cv2.waitKey()

# d. Crop (ambil bagian tengah)
crop = canvas[100:300, 100:300]
cv2.imwrite("output/crop.png", crop)

# 4. Operasi Bitwise dan Aritmatika 

# Background 
background = np.full((400, 400, 3), (200, 230, 255), dtype=np.uint8)

# a. Operasi Bitwise OR → menempelkan rumah ke background
bitwise_or = cv2.bitwise_or(background, canvas)
cv2.imwrite("output/bitwise.png", bitwise_or)

# b. Operasi Aritmatika (cv2.add) → menambah kecerahan
brightened = cv2.add(canvas, (50, 50, 50, 0))
cv2.imwrite("output/final.png", brightened)


