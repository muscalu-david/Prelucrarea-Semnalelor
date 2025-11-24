import numpy as np
import time
import matplotlib.pyplot as plt

def implementare_dft(x):
    N = len(x)
    n = np.arange(N)
    k = n[:, None]
    
    W = np.exp(-2j * np.pi * k * n / N)
    
    X = np.dot(W, x)
    return X

def implementare_fft(x):
    N = len(x)
    
    if N <= 1:
        return x
    
    x_par = implementare_fft(x[::2])
    x_impar = implementare_fft(x[1::2])
    
    k = np.arange(N // 2)
    W_k = np.exp(-2j * np.pi * k / N)
    
    
    X = np.concatenate([
        x_par + W_k * x_impar,
        x_par - W_k * x_impar
    ])
    
    return X


N_vals = [128, 256, 512, 1024, 2048, 4096, 8192] 
num_teste = 10 

dft_times = []
fft_custom_times = []
fft_numpy_times = []

for N in N_vals:
    x = np.random.rand(N)
    
    dft_t = time.time()
    for _ in range(num_teste):
        implementare_dft(x)
    dft_times.append((time.time() - dft_t) / num_teste)
    
    fft_custom_t = time.time()
    for _ in range(num_teste):
        implementare_fft(x)
    fft_custom_times.append((time.time() - fft_custom_t) / num_teste)
    
    fft_numpy_t = time.time()
    for _ in range(num_teste):
        np.fft.fft(x)
    fft_numpy_times.append((time.time() - fft_numpy_t) / num_teste)
    

plt.figure(figsize=(10, 6))

plt.plot(N_vals, dft_times, 'ro-', label='DFT Custom')
plt.plot(N_vals, fft_custom_times, 'bs--', label='FFT Custom')
plt.plot(N_vals, fft_numpy_times, 'g^-', label='FFT NumPy')

plt.yscale('log')
plt.xscale('log')

plt.xlabel('Dimensiunea Vectorului ')
plt.ylabel('Timp de Executie Mediu')
plt.title('Compararea Timpului de Executie')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()

plt.savefig('lab4_ex1.pdf')
plt.show()
