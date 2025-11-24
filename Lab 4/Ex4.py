import numpy as np

f_min = 40.0  
f_max = 200.0 

B = f_max - f_min

k_float = f_max / B
k = np.floor(k_float) 

if k >= 1:
    f_e_min = (2 * f_max) / k
else:
    f_e_min = 2 * f_max

print(f"Frecventa minima (f_min): {f_min} Hz")
print(f"Frecventa maxima (f_max): {f_max} Hz")
print(f"Latimea de banda (B): {B} Hz")
print(f"Valoarea intermediara k_float: {k_float}")
print(f"Valoarea intreaga k: {k}")
print(f"Frecventa minima de esantionare necesara: {f_e_min} Hz")