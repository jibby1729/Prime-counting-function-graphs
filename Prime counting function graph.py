import numpy as np
import matplotlib.pyplot as plt
from sympy import primepi
import math
from scipy import integrate

# Define the range
x_values = np.arange(1, 100001)

# Compute prime counting function pi(x)
pi_values = [primepi(x) for x in x_values]

# Compute x / log(x)
x_log_high_values = [(x / math.log(x)) + (math.sqrt(x)) if x > 1 else 0 for x in x_values]
x_log_low_values = [(x / math.log(x)) - (math.sqrt(x) / math.log(x)) if x > 1 else 0 for x in x_values]

# Define the logarithmic integral function
def log_integral(x):
    if x < 2:
        return 0
    result, _ = integrate.quad(lambda t: 1 / math.log(t), 2, x)
    return result

# Compute the values for the logarithmic integral
log_integral_values = [log_integral(x) for x in x_values]

# Plot the logarithmic integral along with previous functions
plt.figure(figsize=(10, 6))

# Plotpi(x)
plt.plot(x_values, pi_values, linestyle=':', label=r'$\pi(x)$')

# Plot x / log(x)
plt.plot(x_values, x_log_high_values, linestyle=':', label=r'$\frac{x}{\log(x)} + \sqrt{x}\log(x) $')

plt.plot(x_values, x_log_low_values, linestyle=':', label=r'$\frac{x}{\log(x)} - \frac{\sqrt{x}}{\log(x)}$')

# Add legend
plt.legend()

# Label axes
plt.xlabel('x')
plt.ylabel('y')

# Title
plt.title(r'Prime Counting Function $\pi(x)$, $\frac{x}{\log(x)} \pm \frac{\sqrt{x}}{\log(x)}$')

# Show plot
plt.grid()
plt.show()
