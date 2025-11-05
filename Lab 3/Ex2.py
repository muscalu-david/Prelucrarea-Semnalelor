import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
from matplotlib.animation import FuncAnimation

f = 8.0       
fs = 200.0    
T = 2         

N = int(fs * T) 
t = np.linspace(0.0, T, N, endpoint=False)
x = np.cos(2 * np.pi * f * t)

#figura 1
fig1_static, (ax1_s, ax2_s) = plt.subplots(1, 2, figsize=(14, 6))

ax1_s.plot(t, x, color='b')
ax1_s.set_title('Semnal sinusoidal')
ax1_s.set_xlabel('Timp')
ax1_s.set_ylabel('Amplitudine')
ax1_s.grid(True)
ax1_s.set_xlim(0, T)

omega_wrap_fig1 = 1.0
y = x * np.exp(-2 * np.pi * 1j * omega_wrap_fig1 * t)
y_real = y.real
y_imag = y.imag

distance_fig1 = np.abs(y)

points_fig1 = np.array([y_real, y_imag]).T.reshape(-1, 1, 2)
segments_fig1 = np.concatenate([points_fig1[:-1], points_fig1[1:]], axis=1)

norm_fig1 = Normalize(distance_fig1.min(), distance_fig1.max())
lc_fig1 = LineCollection(segments_fig1, cmap='viridis', norm=norm_fig1)
lc_fig1.set_array(distance_fig1[:-1])

line_fig1 = ax2_s.add_collection(lc_fig1)
fig1_static.colorbar(line_fig1, ax=ax2_s, label='Distanta de la origine')

ax2_s.set_title(f'Infasurare cu ω = {omega_wrap_fig1} Hz')
ax2_s.set_xlabel('Partea reala')
ax2_s.set_ylabel('Partea imaginara')
ax2_s.axis('equal')
ax2_s.grid(True)
ax2_s.set_xlim(-1.1, 1.1)
ax2_s.set_ylim(-1.1, 1.1)

plt.tight_layout()
plt.savefig("figura_1_statica.pdf")
print("Graficul static pentru Figura 1 a fost salvat ca 'figura_1_statica.pdf'")
plt.show()


#figura 2

omega_values_fig2 = [2.0, 5.0, f, 15.0]  

fig2_static, axes_fig2_s = plt.subplots(2, 2, figsize=(12, 12))
fig2_static.suptitle('Influenta frecventei de infasurare (ω)', fontsize=16)

for ax, omega in zip(axes_fig2_s.flat, omega_values_fig2):
    z = x * np.exp(-2 * np.pi * 1j * omega * t)
    z_real = z.real
    z_imag = z.imag
    
    distance = np.abs(z)

    points = np.array([z_real, z_imag]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = Normalize(distance.min(), distance.max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    lc.set_array(distance[:-1])
    
    line = ax.add_collection(lc)

    ax.set_title(f'ω = {omega} Hz')
    ax.set_xlabel('Partea reala')
    ax.set_ylabel('Partea imaginara')
    ax.axis('equal')
    ax.grid(True)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("figura_2_statica.pdf")
print("Graficul static pentru Figura 2 a fost salvat ca 'figura_2_statica.pdf'")
plt.show()


#figura 1 animatie

fig_anim1, ax_anim1 = plt.subplots(figsize=(7, 7))
ax_anim1.set_title(f'animatie infasurare (ω = {omega_wrap_fig1} Hz)')
ax_anim1.set_xlabel('Partea reala')
ax_anim1.set_ylabel('Partea imaginara')
ax_anim1.axis('equal')
ax_anim1.grid(True)
ax_anim1.set_xlim(-1.1, 1.1)
ax_anim1.set_ylim(-1.1, 1.1)

lc_anim1 = LineCollection([], cmap='viridis', norm=norm_fig1)
ax_anim1.add_collection(lc_anim1)

current_point_marker1, = ax_anim1.plot([], [], 'ro', label='Punct curent')
ax_anim1.legend()

def init_anim1():
    lc_anim1.set_segments([])
    current_point_marker1.set_data([], [])
    return lc_anim1, current_point_marker1

def animate1(i):
    segments_to_draw = segments_fig1[:i+1]
    colors_to_draw = distance_fig1[:i+1]
    
    lc_anim1.set_segments(segments_to_draw)
    lc_anim1.set_array(colors_to_draw)
    
    current_x = y_real[i+1]
    current_y = y_imag[i+1]
    current_point_marker1.set_data([current_x], [current_y])
    
    return lc_anim1, current_point_marker1

ani1 = FuncAnimation(fig_anim1, animate1, init_func=init_anim1,
                     frames=N-2, interval=20, blit=True)


plt.show()


#figura 2 animatie


all_z_real = []
all_z_imag = []
all_segments = []
all_distances = []

for omega in omega_values_fig2:
    z = x * np.exp(-2 * np.pi * 1j * omega * t)
    z_real = z.real
    z_imag = z.imag
    distance = np.abs(z)
    
    points = np.array([z_real, z_imag]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    all_z_real.append(z_real)
    all_z_imag.append(z_imag)
    all_segments.append(segments)
    all_distances.append(distance)

fig_anim2, axes_anim2 = plt.subplots(2, 2, figsize=(12, 12))
fig_anim2.suptitle('Animatie figura 2', fontsize=16)

plot_lines_anim2 = []
point_markers_anim2 = []

for ax, omega, dist in zip(axes_anim2.flat, omega_values_fig2, all_distances):
    ax.set_title(f'ω = {omega} Hz')
    ax.set_xlabel('Partea reala')
    ax.set_ylabel('Partea imafinara')
    ax.axis('equal')
    ax.grid(True)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    
    norm = Normalize(dist.min(), dist.max())
    lc = LineCollection([], cmap='viridis', norm=norm)
    ax.add_collection(lc)
    
    point_marker, = ax.plot([], [], 'ro')
    
    plot_lines_anim2.append(lc)
    point_markers_anim2.append(point_marker)

def init_anim2():
    for lc in plot_lines_anim2:
        lc.set_segments([])
    for pm in point_markers_anim2:
        pm.set_data([], [])
    return plot_lines_anim2 + point_markers_anim2

def animate2(i):
    for k in range(4):
        segments_to_draw = all_segments[k][:i+1]
        colors_to_draw = all_distances[k][:i+1]
        
        plot_lines_anim2[k].set_segments(segments_to_draw)
        plot_lines_anim2[k].set_array(colors_to_draw)
        
        current_x = all_z_real[k][i+1]
        current_y = all_z_imag[k][i+1]
        point_markers_anim2[k].set_data([current_x], [current_y])
        
    return plot_lines_anim2 + point_markers_anim2

ani2 = FuncAnimation(fig_anim2, animate2, init_func=init_anim2,
                     frames=N-2, interval=20, blit=True)



plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

