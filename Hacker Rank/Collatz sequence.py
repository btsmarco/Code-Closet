# Project Euler #14: Longest Collatz sequence
# hackerrank.com
# Marco Botros
import functools
import time

st = time.time()
CollatzList = []

@functools.lru_cache(maxsize=None)
def CollatzSeq(n):

    if n == 1:
        CollatzList.append(int(n))
        return 1
    elif (n % 2 == 0):
        CollatzList.append(int(n))
        return CollatzSeq(n/2)
    elif (n % 2 == 1):
        CollatzList.append(int(n))
        return CollatzSeq((3*n)+1)


T = int(input())

for t in range(T):
    num = int(input())

    maxLen = 0
    maxNum = 0
    for n in range(1,num+1):
        # print("Collatz seq for",n)
        CollatzSeq(n)

        # print("len",len(CollatzList))
        nLen = len(CollatzList)
        if(maxLen <= nLen):
            maxLen = nLen
            maxNum = n

        CollatzList.clear()


    print(maxNum)

end = time.time()
duration = end - st
print(duration)
