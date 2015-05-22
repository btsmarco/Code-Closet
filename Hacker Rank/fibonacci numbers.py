#!/usr/bin/env python3
# Fibonacci Numbers
# hackerank.com
# Marco Botros

def Fibonacci(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

print(Fibonacci(0))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(8))
