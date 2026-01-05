import numpy as np
import matplotlib.pyplot as plt

B = 1
Ts_values = [1, 1/1.5, 1/2, 1/4]
Fs_values = [1, 1.5, 2, 4]

t_cont = np.linspace(-3, 3, 500)
x_t = (np.sinc(B * t_cont))**2

fig, axes = plt.subplots(4, 1, figsize=(8, 12))
fig.suptitle('Functia sinc^2(t), esantionare si reconstructie')

for i, (Fs, Ts) in enumerate(zip(Fs_values, Ts_values)):
    n_start = int(-3 / Ts)
    n_end = int(3 / Ts)
    n = np.arange(n_start, n_end + 1)
    
    t_n = n * Ts 
    x_n = (np.sinc(B * t_n))**2
    
    x_hat_t = np.zeros_like(t_cont)
    for k in range(len(n)):
        sinc_term = np.sinc((t_cont - t_n[k]) / Ts)
        x_hat_t += x_n[k] * sinc_term
        
    ax = axes[i]
    ax.plot(t_cont, x_t, label='x(t)', color='blue')
    ax.stem(t_n, x_n, linefmt='r:', markerfmt='ro', basefmt=' ', label='Esantioane x[n]')
    ax.plot(t_cont, x_hat_t, label='Reconstructie', color='green', linestyle='--')
    
    ax.set_title(f'Fs = {Fs:.2f} Hz, Ts = {Ts:.2f} s')
    ax.set_xlabel('t [s]')
    ax.set_ylabel('Amplitudine')
    ax.grid(True)
    ax.legend()
    
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("Ex1.pdf")
plt.show()