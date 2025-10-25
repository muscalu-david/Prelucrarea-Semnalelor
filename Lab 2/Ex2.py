import numpy as np
import matplotlib.pyplot as plt

A = 1.0          
f = 5.0          
fs = 1000     
t = np.arange(0, 1, 1/fs)

phases = [0, np.pi/2, np.pi, np.pi/4]
sinusoide = [A * np.sin(2 * np.pi * f * t + phi) for phi in phases]

plt.figure(figsize=(10, 5))
for i, sig in enumerate(sinusoide):
    plt.plot(t, sig,)
plt.title("Semnale sinusoidale cu faze diferite")
plt.xlabel("Timp")
plt.ylabel("Amplitudine")
plt.legend()
plt.grid(True)
plt.show()

x = sinusoide[1]

z = np.random.normal(0, 1, len(x))

SNR_valori = [0.1, 1, 10, 100]

nois = []
for SNR in SNR_valori:
    gamma = np.linalg.norm(x) / (np.sqrt(SNR) * np.linalg.norm(z))
    x_nois = x + gamma * z
    nois.append(x_nois)

plt.figure(figsize=(10, 8))
for i, SNR in enumerate(SNR_valori):
    plt.subplot(len(SNR_valori), 1, i+1)
    plt.plot(t, nois[i], label=f"SNR = {SNR}")
    plt.xlabel("Timp")
    plt.ylabel("Amplitudine")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
