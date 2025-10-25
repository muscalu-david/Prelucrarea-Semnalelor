import numpy as np
import matplotlib.pyplot as plt

A = 2.5         
f = 3.0          
phi = 0.7        
fs = 1000        
t = np.arange(0, 1, 1/fs)  

sinus = A * np.sin(2 * np.pi * f * t + phi)

cosinus = A * np.cos(2 * np.pi * f * t + (phi - np.pi/2))

max_diff = np.max(np.abs(sinus - cosinus))
print(f"Max |sin - cos| = {max_diff:.3e} (≈ 0, diferențe numerice minore)")

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, sinus, 'b')
plt.title('Semnal sinusoidal')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, cosinus, 'r')
plt.title('Semnal cosinus (identic cu sinusul)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.show()
