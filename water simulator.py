import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
amplitude = 1.0
wavelength = 1.0
speed = 1.0
num_waves = 4
num_frames = 100

# Create wave function
def wave_func(x, t, amplitude, wavelength, speed, phase=0):
    k = 2 * np.pi / wavelength
    w = speed * k
    return amplitude * np.sin(k * x - w * t + phase)

# Sum of sine waves
def sum_of_waves(x, t, num_waves):
    result = np.zeros_like(x)
    for i in range(1, num_waves + 1):
        amplitude_i = amplitude / i
        wavelength_i = wavelength / i
        speed_i = speed / i
        phase_i = np.random.uniform(0, 2 * np.pi)
        result += wave_func(x, t, amplitude_i, wavelength_i, speed_i, phase_i)
    return result

# Animation function
fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 1000)
line, = ax.plot(x, sum_of_waves(x, 0, num_waves))

def animate(t):
    y = sum_of_waves(x, t, num_waves)
    line.set_ydata(y)
    return line,

ani = FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True, repeat=True
)

ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-3, 3)
plt.title("Sum of Sine Waves for Water Simulation")
plt.xlabel("X-axis")
plt.ylabel("Wave Amplitude")

plt.show()
