import numpy as np
import matplotlib.pyplot as plt

f_sig1 = 200.0
f_e = 300.0
T_max = 0.03

f_sig2 = abs(f_e - f_sig1)
f_sig3 = abs(f_e + f_sig1)

t_cont = np.linspace(0, T_max, 1000, endpoint=True)
n_samples = int(T_max * f_e) + 1
t_disc = np.linspace(0, T_max, n_samples, endpoint=True)

def sinusoidal_signal(f, t):
    return np.sin(2 * np.pi * f * t)

y_sig1_cont = sinusoidal_signal(f_sig1, t_cont)
y_sig2_cont = sinusoidal_signal(f_sig2, t_cont)
y_sig3_cont = sinusoidal_signal(f_sig3, t_cont)

y_samples = sinusoidal_signal(f_sig1, t_disc)

plt.figure(figsize=(8, 10))
plt.suptitle('Fenomenul de aliere', fontsize=14, fontweight='bold')

plt.subplot(4, 1, 1)
plt.plot(t_cont, y_sig1_cont, color='blue', linewidth=1.5, label=f'{f_sig1} Hz Original')
plt.scatter(t_disc, y_samples, color='yellow', s=50, zorder=5)
plt.title(f'Semnalul original: {f_sig1} Hz. Frecventa de esantionare: {f_e} Hz')
plt.grid(True, linestyle='--', alpha=0.7)
plt.yticks([-1, 0, 1])
plt.ylim(-1.1, 1.1)

plt.subplot(4, 1, 2)
plt.plot(t_cont, y_sig2_cont, color='purple', linewidth=1.5, label=f'{f_sig2} Hz Aliat')
plt.scatter(t_disc, y_samples, color='yellow', s=50, zorder=5)
plt.title(f'Semnal Aliat {f_sig2} Hz')
plt.grid(True, linestyle='--', alpha=0.7)
plt.yticks([-1, 0, 1])
plt.ylim(-1.1, 1.1)

plt.subplot(4, 1, 3)
plt.plot(t_cont, y_sig3_cont, color='green', linewidth=1.5, label=f'{f_sig3} Hz Aliat')
plt.scatter(t_disc, y_samples, color='yellow', s=50, zorder=5)
plt.title(f'Semnal Aliat {f_sig3} Hz')
plt.grid(True, linestyle='--', alpha=0.7)
plt.yticks([-1, 0, 1])
plt.ylim(-1.1, 1.1)

plt.subplot(4, 1, 4)
plt.plot(t_cont, y_sig2_cont, color='red', linewidth=2.0, label=f'{f_sig2} Hz Reconstruit')
plt.scatter(t_disc, y_samples, color='yellow', s=50, zorder=5)
plt.title('Reconstructia esantioanelor')
plt.xlabel('Timp (s)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.yticks([-1, 0, 1])
plt.ylim(-1.1, 1.1)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('lab4_ex2.pdf')
plt.show()