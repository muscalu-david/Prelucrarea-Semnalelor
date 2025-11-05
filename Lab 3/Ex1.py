import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N)
k = n[:, None]  

F = np.exp(-2j * np.pi * k * n / N)        
F_unitary = F / np.sqrt(N)               

for r in range(N):
    fig, axes = plt.subplots(2, 1, sharex=True, figsize=(6, 4))
    
    axes[0].stem(n, F[r].real)
    axes[0].set_title(f"Linia {r} din matricea DFT - Partea reala")
    axes[0].set_ylabel("Partea reala")

    axes[1].stem(n, F[r].imag)
    axes[1].set_title(f"Linia {r} din matricea DFT - Partea imaginara")
    axes[1].set_xlabel("n")
    axes[1].set_ylabel("Partea Imaginara")

    plt.tight_layout()
    plt.show()

I = np.eye(N)

FH_F = F.conj().T @ F
print("Este ortogonala?", np.allclose(FH_F, N * I))

FH_F_u = F_unitary.conj().T @ F_unitary
print("Este unitara?", np.allclose(FH_F_u, I))


