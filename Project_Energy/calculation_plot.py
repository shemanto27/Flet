import math
import numpy as np
import matplotlib.pyplot as plt

L = 10
V = 100
roh = 1.2
A = math.pi * L**2

# Calculate the power values based on the given equation
x = np.linspace(0, V, 100)  # Use linspace for a smooth range of values
y = 0.5 * roh * A * x**3

fig, ax = plt.subplots()
ax.plot(x, y)

plt.xlabel('Velocity (V)')
plt.ylabel('Power (P)')
plt.title('Power vs Velocity')

plt.show()
