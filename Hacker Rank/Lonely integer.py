# Lonely integer
# Hackerrank.com
# Marco Botros

N = int(input())

IntArray = (input()).split()

for i in range(len(IntArray)):
    IntArray[i] = int(IntArray[i])

IntArray.sort()

for i in range(0,len(IntArray),2):
    if(i <= len(IntArray)-2):
        n = i + 1
        if (IntArray[i] != IntArray[n]):
            print(IntArray[i])
            break
    else:
        print(IntArray[i])
        break
