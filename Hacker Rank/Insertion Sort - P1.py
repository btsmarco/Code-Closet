# Insertion Sort
# Hackerrank.com
# Marco Botros

N = int(input())

IArrayStr = (input()).split()
NumList = list(map(int,IArrayStr))

num = NumList[-1]
for i in range((N-1), -1, -1):

    numIndex = NumList.index(num)

    if (NumList[i] > num):
        NumList[numIndex] = NumList[i]
        print(' '.join(map(str,NumList)))
        NumList[i] = num

print(' '.join(map(str,NumList)))
