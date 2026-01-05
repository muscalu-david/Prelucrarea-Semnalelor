import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn
from skimage import data

def aplica_jpeg_cadru(cadru, Q_baza, factor=1.0):
    if len(cadru.shape) != 2:
        return cadru
        
    h, w = cadru.shape
    h_8, w_8 = (h // 8) * 8, (w // 8) * 8
    cadru_crop = cadru[:h_8, :w_8]
    
    Q_scalat = Q_baza * factor
    Q_scalat[Q_scalat < 1] = 1
    
    reconstruit = np.zeros_like(cadru_crop)
    for i in range(0, h_8, 8):
        for j in range(0, w_8, 8):
            bloc = cadru_crop[i:i+8, j:j+8]
            y = dctn(bloc, norm='ortho')
            y_q = np.round(y / Q_scalat)
            y_dq = y_q * Q_scalat
            reconstruit[i:i+8, j:j+8] = idctn(y_dq, norm='ortho')
    return reconstruit

video_complet = data.brain() 
print(f"Dimensiuni video detectate: {video_complet.shape}")

axis_frames = np.argmin(video_complet.shape)
total_frames_available = video_complet.shape[axis_frames]

numar_cadre = min(10, total_frames_available)
factor_compresie = 12.0 

Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

video_original = []
video_comprimat = []
mse_per_cadru = []

for i in range(numar_cadre):
    if axis_frames == 0:
        cadru_orig = video_complet[i, :, :].astype(float)
    else:
        cadru_orig = video_complet[:, :, i].astype(float)
    
    cadru_comp = aplica_jpeg_cadru(cadru_orig, Q_jpeg, factor_compresie)
    
    h_c, w_c = cadru_comp.shape
    mse = np.mean((cadru_orig[:h_c, :w_c] - cadru_comp)**2)
    
    video_original.append(cadru_orig)
    video_comprimat.append(cadru_comp)
    mse_per_cadru.append(mse)

fig = plt.figure(figsize=(15, 10))

indices_to_show = [0, numar_cadre // 2, numar_cadre - 1]
n_cols = len(indices_to_show)

for idx, f_idx in enumerate(indices_to_show):
    plt.subplot(3, n_cols, idx + 1)
    plt.imshow(video_original[f_idx], cmap='gray')
    plt.title(f"Original Cadru {f_idx}")
    plt.axis('off')
    
    plt.subplot(3, n_cols, idx + n_cols + 1)
    plt.imshow(video_comprimat[f_idx], cmap='gray')
    plt.title(f"Comp. MSE: {mse_per_cadru[f_idx]:.1f}")
    plt.axis('off')

plt.subplot(3, 1, 3)
plt.plot(mse_per_cadru, 'b-o', label='MSE per Frame')
plt.axhline(y=np.mean(mse_per_cadru), color='r', linestyle='--', label='MSE Mediu')
plt.xlabel('Cadru')
plt.ylabel('Eroare (MSE)')
plt.title('Evolutia erorii de compresie in timp')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()