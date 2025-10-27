import numpy as np
import matplotlib.pyplot as plt

#Semnal sinusoidal 400 Hz, 1600 esantioane
Fs = 8000  
N = 1600   
f = 400    
t = np.arange(N) / Fs
x_a = np.sin(2 * np.pi * f * t)

plt.figure(figsize=(10, 6))
plt.subplot(3, 2, 1)
plt.plot(t, x_a)
plt.title('(a) Sinusoidal 400 Hz, 1600 eșantioane')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)


#Semnal sinusoidal 800 Hz, durată 3 secunde
Fs = 8000 
f = 800
t = np.arange(0, 3, 1/Fs)
x_b = np.sin(2 * np.pi * f * t)

plt.subplot(3, 2, 2)
plt.plot(t[:500], x_b[:500]) 
plt.title('(b) Sinusoidal 800 Hz, 3 secunde')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)


#Semnal tip sawtooth, frecvență 240 Hz
Fs = 8000
f = 240
t = np.arange(0, 0.02, 1/Fs)
x_c = 2 * (t * f - np.floor(0.5 + t * f)) 

plt.subplot(3, 2, 3)
plt.plot(t, x_c)
plt.title('(c) Sawtooth 240 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)


#Semnal tip square, frecvență 300 Hz
Fs = 8000
f = 300
t = np.arange(0, 0.02, 1/Fs)
x_d = np.sign(np.sin(2 * np.pi * f * t))

plt.subplot(3, 2, 4)
plt.plot(t, x_d)
plt.title('(d) Square 300 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)


#Semnal 2D aleator 128x128
# 
I_random = np.random.rand(128, 128)

plt.subplot(3, 2, 5)
plt.imshow(I_random, cmap='gray')
plt.title('(e) Semnal 2D aleator (128x128)')
plt.axis('off')



#Semnal 2D creat manual (model concentric)
I_custom = np.zeros((128, 128))
center = (64, 64)
for i in range(128):
    for j in range(128):
        dist = np.sqrt((i - center[0])**2 + (j - center[1])**2)
        if 20 < dist < 40:
            I_custom[i, j] = 1  
        elif dist <= 20:
            I_custom[i, j] = 0.5 

plt.subplot(3, 2, 6)
plt.imshow(I_custom, cmap='gray')
plt.title('(f) Semnal 2D personalizat (inel luminos)')
plt.axis('off')

plt.tight_layout()
plt.show()
