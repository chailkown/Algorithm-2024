"""
202111467 차일권
피보나치 수열을 큐를 사용하여 계산하기
"""

from collections import deque

def fibonacci_queue(n):
    if n <= 0:
        return []

    fibonacci = deque([0, 1])

    if n == 1:
        return [0]

    list = [0, 1]
    for i in range(2, n):
        fib_number = fibonacci[0] + fibonacci[1]
        list.append(fib_number)
        fibonacci.popleft()
        fibonacci.append(fib_number)

    return list

print(fibonacci_queue(10))
