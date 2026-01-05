import numpy as np

N = 7
num_coeficienti = N + 1

np.random.seed(42)
coef_p = np.random.randint(-5, 5, size=num_coeficienti)
coef_q = np.random.randint(-5, 5, size=num_coeficienti)

coef_r_conv = np.convolve(coef_p, coef_q)

L_rezultat = len(coef_r_conv)

fft_p = np.fft.fft(coef_p, L_rezultat)
fft_q = np.fft.fft(coef_q, L_rezultat)

fft_r_produs = fft_p * fft_q

coef_r_fft_complex = np.fft.ifft(fft_r_produs)

coef_r_fft = np.round(coef_r_fft_complex.real).astype(int)

print("Calculul coeficientilor produsului p(x)q(x):")
print("-" * 40)
print(f"Coeficientii P(x) (Grad {N}):")
print(coef_p)
print(f"Coeficientii Q(x) (Grad {N}):")
print(coef_q)
print("-" * 40)
print(f"Coeficienti R(x) prin Convolutie Directa (numpy.convolve):")
print(coef_r_conv)
print(f"Coeficienti R(x) prin FFT/IFFT:")
print(coef_r_fft)
print("-" * 40)
print(f"Verificare egalitate: {np.array_equal(coef_r_conv, coef_r_fft)}")