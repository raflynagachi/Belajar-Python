import numpy as np


class image_manipulation:

    def biner(self, citra, threshold, M, N):
        # Membuat citra biner dari citra A berdasarkan nilai ambang
        # (threshold) T yang dispesifikasikan. Ukuran citra adalah M x N.
        # citra_biner adalah tipe data untuk citra biner)
        citra_biner = np.zeros((M, N), dtype=int)
        # print(threshold)
        # print(citra_biner)
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

    def and_boolean(self, citra_biner_a, citra_biner_b, M, N):
        # Membuat citra boolean 'dan' dari citra biner A dan B.
        # Ukuran citra A dan B adalah M x N.
        citra_and_boolean = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                citra_and_boolean[i][j] = citra_biner_a[i][j] and citra_biner_b[i][j]
        return citra_and_boolean

    def or_boolean(self, citra_biner_a, citra_biner_b, M, N):
        # Membuat citra boolean 'or' dari citra biner A dan B.
        # Ukuran citra A dan B adalah M x N.
        citra_or_boolean = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                citra_or_boolean[i][j] = citra_biner_a[i][j] or citra_biner_b[i][j]
        return citra_or_boolean

    def translation(self, citra, M, N, a, b):
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

    def horizontal_flip(self, citra_a, M, N):
        # Flipping horizontal (pencerminan terhadap sumbu-y) terhadap citra A.
        # Ukuran citra adalah M x N. Hasil flipping disimpan di dalam citra B.
        citra_flip = np.zeros((M, N), dtype=int)
        for i in range(M):
            k = 1
            for j in range(N):
                citra_flip[i][N-k] = citra_a[i][j]
                k += 1
        return citra_flip

    def vertical_flip(self, citra_a, M, N):
        # Flipping vertikal (pencerminan terhadap sumbu-X) terhadap citra A.
        # Ukuran citra adalah M x N. Hasil flipping disimpan di dalam citra B.
        citra_flip = np.zeros((M, N), dtype=int)
        k = N-1
        for i in range(M):
            for j in range(N):
                citra_flip[k][j] = citra_a[i][j]
            k -= 1
        return citra_flip

    def zoom_in(self, citra_a, M, N):
        # perbesaran citra A dengan faktor skala 2
        # Ukuran citra adalah M x N. Hasil perbesaran disimpa d dalam citra B.
        m = 0
        n = 0
        citra_zoom = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                if ((m+1) < M) and ((n+1) < N):
                    citra_zoom[m][n] = citra_a[i][j]
                    citra_zoom[m][n+1] = citra_a[i][j]
                    citra_zoom[m+1][n] = citra_a[i][j]
                    citra_zoom[m+1][n+1] = citra_a[i][j]
                    n = n+2
            m = m+2
            n = 0
        return citra_zoom

    def zoom_out(self, citra_a, M, N):
        # pengecilan citra A dengan faktor skala 2
        # Ukuran citra adalah M x N. Hasil perbesaran disimpa d dalam citra B.
        m = 0
        n = 0
        citra_zoom = np.zeros((M, N), dtype=int)
        for i in range(M):
            for j in range(N):
                if ((m+1) < M) and ((n+1) < N):
                    citra_zoom[i][j] = max(
                        citra_a[m][n], citra_a[m+1][n], citra_a[m][n+1], citra_a[m+1][n+1])
                    n = n+2
            m = m+2
            n = 4
        return citra_zoom
