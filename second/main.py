import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0
b = 2

N = 10000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

under_curve = y_random < f(x_random)
monte_carlo_integral = (b - a) * f(b) * np.sum(under_curve) / N

analytical_integral, error = spi.quad(f, a, b)

print(f"Monte Carlo: {monte_carlo_integral}")
print(f"Analytic method: {analytical_integral}")
print(f"Diff: {abs(monte_carlo_integral - analytical_integral)}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.scatter(x_random, y_random, s=1, color="blue", alpha=0.5)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
plt.grid()
plt.show()