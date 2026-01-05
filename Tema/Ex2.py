import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
from skimage import data


def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], 
                      [-.1687, -.3313, .5], 
                      [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return ycbcr

def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], 
                      [1, -0.34414, -0.71414], 
                      [1, 1.772, 0]])
    rgb = im.astype(float)
    rgb[:,:,[1,2]] -= 128
    rgb = rgb.dot(xform.T)
    return np.clip(rgb, 0, 255)

Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

X_rgb = data.astronaut() 


X_ycbcr = rgb2ycbcr(X_rgb)
h, w, c = X_ycbcr.shape
X_comprimat_ycbcr = np.zeros_like(X_ycbcr)

for canal in range(c):
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            bloc = X_ycbcr[i:i+8, j:j+8, canal]
            
            y = dctn(bloc, norm='ortho')
            y_quant = np.round(y / Q_jpeg)
            y_dequant = y_quant * Q_jpeg
            X_comprimat_ycbcr[i:i+8, j:j+8, canal] = idctn(y_dequant, norm='ortho')

X_final_rgb = ycbcr2rgb(X_comprimat_ycbcr).astype(np.uint8)

plt.figure(figsize=(12, 6))
plt.subplot(121).imshow(X_rgb)
plt.title('Original RGB')
plt.axis('off')

plt.subplot(122).imshow(X_final_rgb)
plt.title('JPEG Color')
plt.axis('off')

plt.tight_layout()
plt.show()