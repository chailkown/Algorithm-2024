def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

import numpy as np

def fibonacci_matrix_power(n):
    F = np.array([[1, 1], [1, 0]], dtype=object)
    if n == 0:
        return 0
    power = np.linalg.matrix_power(F, n - 1)
    return power[0][0]


import time
import matplotlib.pyplot as plt

def fibonacci_function(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    return result, end_time - start_time

n_values = list(range(1, 31))

recursive_times = []
iterative_times = []
matrix_power_times = []

for n in n_values:
    _, recursive_time = fibonacci_function(fibonacci_recursive, n)
    _, iterative_time = fibonacci_function(fibonacci_iterative, n)
    _, matrix_power_time = fibonacci_function(fibonacci_matrix_power, n)
    recursive_times.append(recursive_time)
    iterative_times.append(iterative_time)
    matrix_power_times.append(matrix_power_time)

plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, iterative_times, label='Iterative')
plt.plot(n_values, matrix_power_times, label='Matrix Power')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Execution Time for Fibonacci Algorithms')
plt.legend()
plt.show()
