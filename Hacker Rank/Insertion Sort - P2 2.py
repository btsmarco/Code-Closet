# Insertion Sort - Part 2
# Hackerrank.com
# Marco Botros

N = int(input())

NumList = (input()).split()
NumList = list(map(int,NumList))

for i in range(N-1):
    i = i if (i < N-1) else i-1
    k = i+1

    while (NumList[i] > NumList[k]):
        temp = NumList[i]
        NumList[i] = NumList[k]
        NumList[k] = temp

        i -= 1
        k -= 1
        if(i == 0):
            k = 1
        elif (i < 0):
            break

    print(' '.join(map(str,NumList)))
