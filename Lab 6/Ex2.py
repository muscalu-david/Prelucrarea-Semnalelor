import numpy as np
import matplotlib.pyplot as plt

N = 100
num_iteratii = 3
titluri = ['Semnal Initial', 'Convolutie 1', 'Convolutie 2', 'Convolutie 3']

np.random.seed(42)
x_aleator = np.random.uniform(-1, 1, N)

semnale_aleator = [x_aleator]
x_curent_aleator = x_aleator

for i in range(num_iteratii):
    x_nou = np.convolve(x_curent_aleator, x_aleator)
    semnale_aleator.append(x_nou)
    x_curent_aleator = x_nou

fig1, axes1 = plt.subplots(4, 1, figsize=(10, 12))
fig1.suptitle('Efectul convolutiei iterative: Semnal Aleator', fontsize=16)

for i, semnal in enumerate(semnale_aleator):
    ax = axes1[i]
    ax.plot(semnal)
    ax.set_title(f'{titluri[i]} (Lungime: {len(semnal)})')
    ax.set_ylabel('Amplitudine')
    ax.grid(True)
    
axes1[-1].set_xlabel('Index n')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("Ex2_convolutie_aleator.pdf")

M = 20
x_bloc = np.zeros(N)
x_bloc[:M] = 1

semnale_bloc = [x_bloc]
x_curent_bloc = x_bloc

for i in range(num_iteratii):
    x_nou = np.convolve(x_curent_bloc, x_bloc)
    semnale_bloc.append(x_nou)
    x_curent_bloc = x_nou

fig2, axes2 = plt.subplots(4, 1, figsize=(10, 12))
fig2.suptitle('Efectul convolutiei iterative: Semnal Bloc Rectangular', fontsize=16)

for i, semnal in enumerate(semnale_bloc):
    ax = axes2[i]
    ax.plot(semnal)
    ax.set_title(f'{titluri[i]} (Lungime: {len(semnal)})')
    ax.set_ylabel('Amplitudine')
    ax.grid(True)
    
axes2[-1].set_xlabel('Index n')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("Ex2_convolutie_bloc.pdf")

plt.show()