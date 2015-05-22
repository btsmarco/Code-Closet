# Binary Search
# Marco Botros
from math import ceil

num = int(input())

strList = input().split()
nList = list(map(int,strList))

nList.sort()

print(nList)

startIn = 0
endIn = len(nList)-1
found = False

while startIn<=endIn and not found:
    half = (endIn + startIn)//2

    halfElem = nList[half]

    if (num > halfElem):
        startIn = half + 1
    elif (num == halfElem):
        found = True
    elif (num < halfElem):
        endIn = half - 1

print("Item",num,"was found:", found)
