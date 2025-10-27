import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.03, 0.0005)

x_t = np.cos(520 * np.pi * t + np.pi/3)
y_t = np.cos(280 * np.pi * t - np.pi/3)
z_t = np.cos(120 * np.pi * t + np.pi/3)

plt.figure(figsize=(10, 7))

plt.subplot(3, 1, 1)
plt.plot(t, x_t)
plt.title('Semnalul x(t) = cos(520πt + π/3)')
plt.xlabel('t')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, y_t)
plt.title('Semnalul y(t) = cos(280πt - π/3)')
plt.xlabel('t')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, z_t)
plt.title('Semnalul z(t) = cos(120πt + π/3)')
plt.xlabel('t')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.show()


Fs = 200  # Hz
Ts = 1 / Fs
n = np.arange(0, 0.03, Ts)

x_n = np.cos(520 * np.pi * n + np.pi/3)
y_n = np.cos(280 * np.pi * n - np.pi/3)
z_n = np.cos(120 * np.pi * n + np.pi/3)

plt.figure(figsize=(10, 7))

plt.subplot(3, 1, 1)
plt.stem(n, x_n, basefmt=" ")
plt.title('Semnalul eșantionat x[n]')
plt.xlabel('n')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, y_n, basefmt=" ")
plt.title('Semnalul eșantionat y[n]')
plt.xlabel('n')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, z_n, basefmt=" ")
plt.title('Semnalul eșantionat z[n]')
plt.xlabel('n')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.show()
