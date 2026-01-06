import numpy as np
import matplotlib.pyplot as plt

def plot_signal_and_spectrum(X, title, filename):
    Y = np.fft.fft2(X)
    Y_shifted = np.fft.fftshift(Y)
    spectrum_db = 20 * np.log10(np.abs(Y_shifted) + 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.imshow(X, cmap='gray')
    ax1.set_title(f'Imagine: {title}')
    im2 = ax2.imshow(spectrum_db, cmap='magma')
    ax2.set_title(f'Spectru (Log)')
    plt.colorbar(im2, ax=ax2)
    plt.tight_layout()
    
    # Salvarea in format PDF
    plt.savefig(f"{filename}.pdf")
    plt.show()

N = 128
n1, n2 = np.meshgrid(np.arange(N), np.arange(N))

# 1: x_{n1,n2} = sin(2*pi*n1*2/N + 2*pi*n2*3/N)
# Avem variatie si pe orizontala (n1) si pe verticala (n2).
# Rezulta o imagine cu dungi inclinate si doua puncte simetrice pe diagonala in spectru.
x1 = np.sin(2 * np.pi * (2 * n1 / N + 3 * n2 / N))
plot_signal_and_spectrum(x1, "sin(2pi n1 + 3pi n2)", "Ex1_1")

# 2: Suma de frecvente independente
# sin(4*pi*n1/N) produce dungi verticale; cos(6*pi*n2/N) produce dungi orizontale.
# Combinarea lor creeaza un model de tip carou.
x2 = np.sin(2 * np.pi * (4 * n1 / N)) + np.cos(2 * np.pi * (6 * n2 / N))
plot_signal_and_spectrum(x2, "sin(4pi n1) + cos(6pi n2)", "Ex1_2")

# 3: Energie doar pe axa verticala a spectrului
# m1=0 inseamna frecventa zero pe orizontala. Variatia este pur verticala.
# Rezultatul vizual este linii orizontale paralele.
Y3 = np.zeros((N, N), dtype=complex)
Y3[0, 5] = Y3[0, N-5] = 1 
x3 = np.fft.ifft2(Y3).real
plot_signal_and_spectrum(x3, "Y[0,5] = Y[0,N-5] = 1", "Ex1_3")

# 4: Energie doar pe axa orizontala a spectrului
# m2=0 inseamna frecventa zero pe verticala. Variatia este pur orizontala.
# Rezultatul vizual este linii verticale paralele.
Y4 = np.zeros((N, N), dtype=complex)
Y4[5, 0] = Y4[N-5, 0] = 1
x4 = np.fft.ifft2(Y4).real
plot_signal_and_spectrum(x4, "Y[5,0] = Y[N-5,0] = 1", "Ex1_4")

# 5: Energie pe ambele axe (diagonala)
# m1=5 si m2=5
Y5 = np.zeros((N, N), dtype=complex)
Y5[5, 5] = Y5[N-5, N-5] = 1
x5 = np.fft.ifft2(Y5).real
plot_signal_and_spectrum(x5, "Y[5,5] = Y[N-5,N-5] = 1", "Ex1_5")