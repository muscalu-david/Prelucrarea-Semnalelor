import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

X = datasets.face(gray=True)

def get_snr(original, compressed):
    signal_power = np.mean(original.astype(float)**2)
    noise_power = np.mean((original.astype(float) - compressed)**2)
    return 10 * np.log10(signal_power / noise_power)

def compress_until_snr(image, target_snr):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    
    Y = np.fft.fft2(image)
    Y_shifted = np.fft.fftshift(Y)
    
    y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
    
    for r in range(1, crow):
        mask = x*x + y*y <= r*r
        Y_comp_shifted = Y_shifted * mask
        
        Y_comp = np.fft.ifftshift(Y_comp_shifted)
        X_comp = np.fft.ifft2(Y_comp).real
        
        current_snr = get_snr(image, X_comp)
        
        if current_snr >= target_snr:
            return X_comp, current_snr, r
            
    return X_comp, current_snr, r

PRAG_SNR_AUTOIMPUS = 10 

X_res, snr_final, raza_gasita = compress_until_snr(X, PRAG_SNR_AUTOIMPUS)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(X, cmap='gray')
ax[0].set_title("Originala")
ax[1].imshow(X_res, cmap='gray')
ax[1].set_title(f"Comprimata (SNR atins: {snr_final:.2f} dB)")

plt.tight_layout()
plt.savefig("Ex2.pdf")
plt.show()

