# The bisection method is a technique for finding solutions (roots) to equations with a single
# unknown variable. Given a polynomial function f, try to find an initial interval off by
# random probe. Store all the updates in an Numpy array. Plot the root finding process using
# the matplotlib/pyplot library.
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - x - 2

a, b = np.random.uniform(-10, 0), np.random.uniform(1, 10)
while f(a) * f(b) > 0:
    a, b = np.random.uniform(-10, 0), np.random.uniform(1, 10)

updates = []

for _ in range(20):
    c = (a + b) / 2
    updates.append(c)
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

updates = np.array(updates)

print("Final root approximation:", updates[-1])

x = np.linspace(-3, 3, 400)
y = f(x)

plt.plot(x, y)
plt.axhline(0, color='black', linestyle='--')
plt.plot(updates, f(updates), 'ro-')
plt.title("Bisection Method Root Finding")
plt.show()

