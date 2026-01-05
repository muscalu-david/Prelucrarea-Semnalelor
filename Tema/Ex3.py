import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
from scipy.datasets import ascent

def aplica_jpeg(imagine, Q_baza, factor):
    h, w = imagine.shape
    Q_scalat = Q_baza * factor
    Q_scalat[Q_scalat < 1] = 1 
    
    img_reconstruita = np.zeros_like(imagine)
    
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            bloc = imagine[i:i+8, j:j+8]
            y = dctn(bloc, norm='ortho')
            y_q = np.round(y / Q_scalat)
            y_dq = y_q * Q_scalat
            img_reconstruita[i:i+8, j:j+8] = idctn(y_dq, norm='ortho')
            
    return img_reconstruita

X = ascent().astype(float)
Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

prag_mse_tinta = 50.0 
factor_curent = 0.1
pas = 0.2
mse_obtinut = 0
imagine_finala = None

print(f"Cautam factorul de compresie pentru MSE tinta: {prag_mse_tinta}")

while mse_obtinut < prag_mse_tinta:
    img_temp = aplica_jpeg(X, Q_jpeg, factor_curent)
    mse_obtinut = np.mean((X - img_temp)**2)
    
    if mse_obtinut >= prag_mse_tinta:
        imagine_finala = img_temp
        break
    
    factor_curent += pas
    if factor_curent > 50: 
        break

print(f"S-a oprit la factorul: {factor_curent:.2f}")
print(f"MSE final: {mse_obtinut:.2f}")

plt.figure(figsize=(12, 6))
plt.subplot(121).imshow(X, cmap='gray')
plt.title('Original')
plt.subplot(122).imshow(imagine_finala, cmap='gray')
plt.title(f'Comprimat (MSE prag: {prag_mse_tinta})')
plt.show()