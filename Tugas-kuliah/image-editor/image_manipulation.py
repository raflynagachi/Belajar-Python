import numpy as np


class image_manipulation:

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

    def addition(self, citra_a, citra_b, M, N):
        # Menjumlahkan dua buah citra A dan B menjadi citra baru, C.
        # Citra A, B, dan C masing-masing berukuran M x N.
        citra_add = np.zeros((M, N), dtype=int)
        temp = 0
        for i in range(M):
            for j in range(N):
                temp = citra_a[i][j]+citra_b[i][j]
                if temp > 255:
                    citra_add[i][j] = 0
                else:
                    citra_add[i][j] = temp
        return citra_add

    def substraction(self, citra_a, citra_b, M, N):
        # Mengurangkan dua buah citra A dan B menajdi citra baru, C.
        # Citra A, B, dan C berukuran M x N.
        citra_sub = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                citra_sub[i][j] = citra_a[i][j] - citra_b[i][j]
                if citra_sub[i][j] != 0:
                    citra_sub[i][j] = 255
        return citra_sub

    def multiplication(self, citra_a, citra_b, M, N):
        # Mengalikan citra A dengan citra B menjadi citra C.
        # Citra A, matriks B, dan hasil perkalian C berukuran M x N.
        citra_mult = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                for k in range(N):
                    citra_mult[i][j] = citra_a[i][j] * citra_b[i][j]
                    # clipping
                    if citra_mult[i][j] < 0:
                        citra_mult[i][j] = 0
                    elif citra_mult[i][j] > 255:
                        citra_mult[i][j] = 255
        return citra_mult

    def not_boolean(self, citra_biner_a, M, N):
        # Membuat citra komplemen dari citra biner A.
        # Komplemennya disimpan di dalam B. Ukuran citra A
        # adalah M x N.
        citra_not_boolean = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                citra_not_boolean[i][j] = not citra_biner_a[i][j]
        return citra_not_boolean

    def translation(self, citra, M, N, b, a):
        # Mentranslasi citra A sejauh a, b menjadi citra B. Ukuran citra M x N.
        citra_translation = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                if ((i+a) < M) and ((j+b) < N) and ((i+a) >= 0) and ((j+b) >= 0):
                    citra_translation[i][j] = citra[i+a][j+b]
        return citra_translation

    def rotation90CCW(self, citra, M, N):
        # Rotasi citra A sejauh 90 berlawanan arah jarum jam (CCW = Clock Counterwise).
        # Ukuran citra adalah M x N. Hasil rotasi disimpan di dalam citra B.
        citra_rotated = np.zeros((M, N), dtype=int)
        for i in range(M):
            k = N-1
            for j in range(N):
                citra_rotated[k][i] = citra[i][j]
                k -= 1
        return citra_rotated

    def rotation90CW(self, citra, M, N):
        # Rotasi citra A sejauh 90 searah jarum jam (CW = Clockwise).
        # Ukuran citra adalah M x N. Hasil rotasi disimpan di dalam citra B.
        citra_rotated = np.zeros((M, N), dtype=int)
        k = N-1
        for i in range(M):
            for j in range(N):
                citra_rotated[j][k] = citra[i][j]
            k -= 1
        return citra_rotated
