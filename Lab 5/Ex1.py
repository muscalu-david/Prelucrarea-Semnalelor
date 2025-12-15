import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt(r"C:\Users\David\Desktop\Facultate\An 3\Semnale\Lab 5\archive\Train.csv", delimiter=',', skip_header=1, usecols = 2)

#a

fs = 1/3600

#b

ts = 1/fs
perioada_acoperita = len(x) * ts
print(f"Perioada acoperita: {perioada_acoperita}s sau {len(x)} ore sau {len(x)/24} zile sau {len(x)/24/265} ani")

#c

B = fs/2 
print(f"Frecventa maxima prezenta in semnal: {B} Hz")

#d

N = len(x)
X_complex = np.fft.fft(x)
X_spectru = np.abs(X_complex / N)
X_spectru_pozitiv = X_spectru[:N//2]

f_Hz = fs * np.linspace(0, N/2, N//2, endpoint=False) / N

plt.figure(figsize=(10, 4))
plt.plot(f_Hz, X_spectru_pozitiv)
plt.title('Modulul Transformatei Fourier')
plt.xlabel('Frecventa (Hz)')
plt.ylabel('Amplitudine Normalizata')
plt.grid(True)
plt.savefig("Ex1_d.pdf")
plt.show()

#e

media_x = np.mean(x)

#Eliminare:
x_centrat = x - media_x

X_complex_centrat = np.fft.fft(x_centrat)
X_spectru_centrat = np.abs(X_complex_centrat / N)
X_spectru_centrat_pozitiv = X_spectru_centrat[:N//2]

plt.figure(figsize=(10, 4))
plt.plot(f_Hz, X_spectru_centrat_pozitiv)
plt.xlabel("Frecvente [Hz]")
plt.ylabel("|X(f)|")
plt.title("Transformata Fourier a semnalului dupa eliminarea componentei continue")
plt.grid(True)
plt.xlim(0, 0.00014) 
plt.savefig("Ex1_e_FT_centrat.pdf")
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(np.arange(0, N, 1), x_centrat)
plt.xlabel("Esantion")
plt.ylabel("Amplitudine centrata")
plt.title("Semnalul fara comp continua")
plt.grid(True)
plt.savefig("Ex1_e_semnal_centrat.pdf")
plt.show()

#f

indici = np.argsort(X_spectru_centrat_pozitiv)[-4:][::-1]

for i in indici:
    print(f"Frecventa: {f_Hz[i]:.5e} Hz, |X| = {X_spectru_centrat_pozitiv[i]:.5f}")

#g

start_index = 1056
durata_luna = 720
end_index = start_index + durata_luna

if end_index > N:
    start_index = 0
    end_index = min(N, durata_luna)


plt.figure(figsize=(12, 6))
plt.plot(np.arange(start_index, end_index), x[start_index:end_index])
plt.title('Vizualizare Trafic (O Luna, incepand Luni)')
plt.xlabel('Esantion (Ora)')
plt.ylabel('Numar masini')
plt.grid(True)
plt.savefig("Ex1_g.pdf")
plt.show()

#h

#i

# Justificare: Alegem fc = 0.00005 Hz. Aceasta valoare este suficient de mare pentru a pastra 
# ciclul zilnic (1.157e-5 Hz)

fc_Hz = 0.00005 

X_complex_centrat = np.fft.fft(x_centrat)

frequencies_full = np.fft.fftfreq(N, d=1/fs) 

mask = np.abs(frequencies_full) < fc_Hz

X_filtrat_complex = X_complex_centrat * mask

x_filtrat_centrat = np.fft.ifft(X_filtrat_complex)
x_filtrat_centrat = np.real(x_filtrat_centrat) 

x_filtrat = x_filtrat_centrat + media_x


plt.figure(figsize=(12, 6))
plt.plot(np.arange(start_index, end_index), x[start_index:end_index], label='Semnal Brut', alpha=0.5)
plt.plot(np.arange(start_index, end_index), x_filtrat[start_index:end_index], label=f'Semnal Filtr. (fc={fc_Hz:.2e} Hz)', color='red')
plt.title('Comparatie: Semnal Brut vs. Semnal Filtrate (Eliminare Frecvente Inalte)')
plt.xlabel('Esantion (Ora)')
plt.ylabel('Numar masini')
plt.legend()
plt.grid(True)
plt.savefig("Ex1_i.pdf")
plt.show()