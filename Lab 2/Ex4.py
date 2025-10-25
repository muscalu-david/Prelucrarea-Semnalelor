import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth  

fs = 1000        
t = np.arange(0, 1, 1/fs)  

A1 = 1.0         
f1 = 5.0         
x1 = A1 * np.sin(2 * np.pi * f1 * t)

A2 = 1.0         
f2 = 3.0         
x2 = A2 * sawtooth(2 * np.pi * f2 * t)

x_sum = x1 + x2

plt.figure(figsize=(10, 4))
plt.plot(t, x_sum, 'g')
plt.title("Suma celor două semnale (sinus + sawtooth)")
plt.xlabel("Timp [s]")
plt.ylabel("Amplitudine")
plt.grid(True)
plt.show()
