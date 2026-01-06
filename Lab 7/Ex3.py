import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

X = datasets.face(gray=True).astype(float)

pixel_noise = 50
noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=X.shape)
X_noisy = X + noise

signal_power = np.mean(X**2)
noise_power_before = np.mean((X - X_noisy)**2)
snr_before = 10 * np.log10(signal_power / noise_power_before)

Y = np.fft.fft2(X_noisy)
Y_shifted = np.fft.fftshift(Y)

rows, cols = X.shape
crow, ccol = rows // 2, cols // 2
y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
radius = 50
mask = x*x + y*y <= radius*radius

Y_denoised_shifted = Y_shifted * mask
Y_denoised = np.fft.ifftshift(Y_denoised_shifted)
X_denoised = np.fft.ifft2(Y_denoised).real

noise_power_after = np.mean((X - X_denoised)**2)
snr_after = 10 * np.log10(signal_power / noise_power_after)

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

ax[0].imshow(X, cmap='gray')
ax[0].set_title("Originala")

ax[1].imshow(X_noisy, cmap='gray')
ax[1].set_title(f"Cu Zgomot (SNR: {snr_before:.2f} dB)")

ax[2].imshow(X_denoised, cmap='gray')
ax[2].set_title(f"Dupa Filtrare (SNR: {snr_after:.2f} dB)")

plt.tight_layout()
plt.savefig("Ex3.pdf")
plt.show()

print(f"SNR inainte de filtrare: {snr_before:.2f} dB")
print(f"SNR dupa filtrare: {snr_after:.2f} dB")