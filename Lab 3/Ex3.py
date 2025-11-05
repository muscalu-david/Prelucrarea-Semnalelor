import numpy as np
import matplotlib.pyplot as plt

fs = 200.0  
T = 2.0     
N = int(fs * T) 
t = np.linspace(0.0, T, N, endpoint=False) 

f1 = 15.0  
A1 = 1.5

f2 = 40.0  
A2 = 0.75

f3 = 80.0  
A3 = 2.0

x = (A1 * np.cos(2 * np.pi * f1 * t) +
     A2 * np.cos(2 * np.pi * f2 * t) +
     A3 * np.cos(2 * np.pi * f3 * t))

omega_range = np.arange(0, 100.25, 0.25)

exponent_matrix = -2.0 * np.pi * 1j * np.outer(omega_range, t)

M = np.exp(exponent_matrix)

X_omega = M @ x

X_magnitude = np.abs(X_omega)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(t, x, color='b')
ax1.set_title('Semnalul compus')
ax1.set_xlabel('Timp')
ax1.set_ylabel('Amplitudine')
ax1.grid(True)
ax1.set_xlim(0, 0.2) 

ax2.plot(omega_range, X_magnitude, color='r')
ax2.set_title('Modulul Transformatei Fourier')
ax2.set_xlabel('Frecventa')
ax2.set_ylabel('Magnitudine')
ax2.grid(True)
ax2.set_xlim(0, 100)

plt.tight_layout()
plt.savefig("figura_3_transformata_ex3.pdf")
plt.show()