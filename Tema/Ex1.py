import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
from scipy.datasets import ascent

Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

X = ascent().astype(float)
h, w = X.shape

X_final = np.zeros((h, w))

total_nnz_init = 0
total_nnz_jpeg = 0

for i in range(0, h, 8):
    for j in range(0, w, 8):
        bloc = X[i:i+8, j:j+8]
        
        y = dctn(bloc, norm='ortho')
        y_quant = np.round(y / Q_jpeg)
        
        total_nnz_init += np.count_nonzero(y)
        total_nnz_jpeg += np.count_nonzero(y_quant)
        
        y_dequant = y_quant * Q_jpeg
        bloc_reconstruit = idctn(y_dequant, norm='ortho')
        
        X_final[i:i+8, j:j+8] = bloc_reconstruit

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(X, cmap=plt.cm.gray)
plt.title('Imagine Originala')
plt.axis('off')

plt.subplot(122)
plt.imshow(X_final, cmap=plt.cm.gray)
plt.title('Imagine Comprimata JPEG')
plt.axis('off')

plt.tight_layout()
plt.show()
