# Insertion Sort - Part 2
# Hackerrank.com
# Marco Botros

N = int(input())

NumList = (input()).split()
NumList = list(map(int,NumList))

for i in range(N-1):
    init = NumList[i]
    comp = NumList[i+1]
    s = i

    while (init > comp):
        NumList[s] = comp
        NumList[s+1] = init

        if(s<= 1):
            s -= 1
            init = NumList[s]
            comp = NumList[s+1]
        else:
            break

    print(' '.join(map(str,NumList)))

num = NumList[-2]
for i in range((N-1), -1, -1):

    numIndex = NumList.index(num)

    if (NumList[i] > num):
        NumList[numIndex] = NumList[i]
        NumList[i] = num

print(' '.join(map(str,NumList)))
