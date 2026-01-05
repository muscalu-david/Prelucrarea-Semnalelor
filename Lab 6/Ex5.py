import numpy as np
import matplotlib.pyplot as plt

def fereastra_dreptunghiulara(N):
    return np.ones(N)

def fereastra_hanning(N):
    n = np.arange(N)
    return 0.5 * (1 - np.cos(2 * np.pi * n / N))

f = 100
A = 1
phi = 0
Nw = 200
fs = 1000

t = np.arange(Nw) / fs
x = A * np.sin(2 * np.pi * f * t + phi)

w_rect = fereastra_dreptunghiulara(Nw)
w_hann = fereastra_hanning(Nw)

x_rect = x * w_rect
x_hann = x * w_hann

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, x_rect, 'b', label='Sinusoida + Fereastra Dreptunghiulara')
plt.title('Efectul Ferestrei Dreptunghiulare (f=100Hz)')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, x_hann, 'r', label='Sinusoida + Fereastra Hanning')
plt.title('Efectul Ferestrei Hanning (f=100Hz)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("Ex5_ferestre_hanning_rect.pdf")
plt.show()