import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def bisection(a, b, tol=1e-5, max_iter=100):
    updates = []
    if f(a) * f(b) >= 0:
        return None, np.array(updates)
    for _ in range(max_iter):
        c = (a + b) / 2.0
        updates.append(c)
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, np.array(updates)

a, b = 0.5, 3.5
root, updates = bisection(a, b)

x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.plot(updates, f(updates), 'ro-', label='Bisection Steps')
plt.title('Bisection Method Root Finding')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
