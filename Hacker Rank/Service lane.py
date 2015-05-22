# Service Lane
# Hackerrank.com
# Marco Botros

# 1. Save inputs

# length in units
Inp = (input()).split(' ')
N = int(Inp[0])
T = int(Inp[1])

width = (input()).split()
for n in range(len(width)):
        element = width[n]
        width[n] = int(element)

# 2. Functions
def CommonWidth(WidthArray,i,j):
    V = 3
    Array = WidthArray[i:j+1]
    for n in Array:
        res = n - V
        if res == -1:
            V = V - 1
        elif res >= 0:
            continue
        else:
            V = 1
    return V


# 3. Main
for loop in range(T):
    TempValues = (input()).split()
    i = int(TempValues[0])
    j = int(TempValues[1])

    result = CommonWidth(width,i,j)

    print (result)
