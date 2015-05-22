from operator import xor

L = int (input())
R = int (input())

maxXor = 0
A = L
B = A

while (True):
    if (B <= R):
        res = xor (A,B)
        maxXor = max (res, maxXor)

        B += 1
    elif (B > R):
        A += 1
        B = A

    if ( A > R):
        break

print (maxXor)
