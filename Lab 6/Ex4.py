import numpy as np

n = 20
d = 5

np.random.seed(42) 
t = np.arange(n)
x = np.exp(-0.5 * ((t - 10) / 3)**2) + 0.1 * np.random.randn(n) 

y = np.roll(x, d)

FFT_x = np.fft.fft(x)
FFT_y = np.fft.fft(y)

FFT_corelatie = FFT_x.conjugate() * FFT_y
r1 = np.fft.ifft(FFT_corelatie)
r1_real = r1.real

deplasare_recuperata_1 = np.argmax(r1_real)

FFT_diviziune = FFT_y / FFT_x

r2 = np.fft.ifft(FFT_diviziune)
r2_real = r2.real

deplasare_recuperata_2 = np.argmax(r2_real)

print(f"Deplasarea circulara aleasa (d): {d}")
print("-" * 40)
print(f"Deplasare recuperata (Formula 1 - Corelatie Circulara): {deplasare_recuperata_1}")
print(f"Deplasare recuperata (Formula 2 - Factor de Deplasare): {deplasare_recuperata_2}")
print("-" * 40)
print("Diferenta dintre cele doua formule:")
print("Formula 1 calculeaza Corelatia Circulara: maximul indica deplasarea, iar rezultatul este un semnal netezit.")
print("Formula 2 calculeaza Factorul de Deplasare: rezultatul este un Impuls Unitar la indexul deplasarii d.")