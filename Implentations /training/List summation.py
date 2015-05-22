#!/usr/bin/env python3
# List summation, recursion
# Marco Botros

def addlist(inp):
    if (len(inp) == 1):
        return inp[0]
    else:
        return inp[0] + addlist(inp[1:])

print(addlist([1,2,3,4,5,6,7]))
