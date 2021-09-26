from numpy import dtype
import numpy as np


class image_manipulation:
    # def __init__(self, image):
    #     self.image = image

    # def set_image(self, image):
    #     self.image = image

    def biner(self, citra, threshold, M, N):
        # Membuat citra biner dari citra A berdasarkan nilai ambang
        # (threshold) T yang dispesifikasikan. Ukuran citra adalah M x N.
        # citra_biner adalah tipe data untuk citra biner)
        citra_biner = np.zeros((M, N), dtype=int)
        print(threshold)
        print(citra_biner)
        for i in range(M):
            for j in range(N):
                if citra[i][j] < threshold:
                    citra_biner[i][j] = 1
                else:
                    citra_biner[i][j] = 0
        return citra_biner

    def negatif(self, citra, M, N):
        # Membuat citra negatif dari citra A. Hasilnya disimpan di
        # dalam citra B. Ukuran citra adalah M x N.
        citra_negatif = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                citra_negatif[i][j] = 255 - citra[i][j]
        return citra_negatif

    def grayscale(self, citra, M, N):
        citra_abu = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                citra_abu[i][j] = int(0.299*citra[i][j][0]) + \
                    int(0.587*citra[i][j][1]) + int(0.114*citra[i][j][2])
        return citra_abu

    def image_brightening(self, citra, b, M, N):
        # Pencerahan citra dengan menjumlahkan setiap pixel di dalam citra A dengan
        # sebuah skalar b. Hasil disimpan di dalam citra B. Citra berukuran M x N.
        citra_bright = np.zeros((M, N), dtype=int)
        temp = 0
        for i in range(M):
            for j in range(N):
                temp = citra[i][j] + b
                if temp < 0:
                    temp = 0
                else:
                    if temp > 255:
                        citra_bright[i][j] = 255
                    else:
                        citra_bright[i][j] = temp
        return citra_bright
