# Maximise Sum
# hackerrank.com
# Marco Botros

def FindInList(inList, possibleSums,listMax,M):

    done = False
    # Try to find the integers themselves in the list
    for i in possibleSums:
        if (i < listMax):
            for k in inList:
                if (i == k):
                    print(i%M)
                    done = True
                    break
    return done

# The function returns information about the list, Sum, Max and Min values
def ProcessList(inList):

    listSum = sum(inList)
    listMax = max(inList)
    listMin = min(inList)

    return(listSum,listMin,listMax)

def ExhaustiveSum(inList,M,maxNum):
    sumMax = 0
    for x in range(len(inList)):
        for y in range(len(inList)):
            theSum = sum(inList[x:y])
            sumMax = max(sumMax,theSum % M)
            if(sumMax == maxNum):
                return sumMax

    return sumMax

def main():
    T = int(input())

    for i in range(T):
        inputList = list(map(int,(input()).split()))

        N = inputList[0]
        M = inputList[1]

        inputList2 = list(map(int,(input()).split()))

        maxNum = M - 1
        listSum,listMin,listMax = ProcessList(inputList2)

        possibleSums = [(maxNum + (M * i)) for i in range(int(listSum/M)) ]

        # Try # 1
        if (listSum % M == maxNum):
            print(listSum % M)
            continue

        if(listMin == possibleSums[0]):
            print(listMin % M)
            continue

        if(possibleSums.count(listMax)):
            print(listMax % M)
            continue

        # Try # 2
        #done = FindInList(inputList2,possibleSums,listMax,M)
        #if (done == True):
        #    continue

        # Try # 3
        sumMax = ExhaustiveSum(inputList2,M,maxNum)
        print(sumMax)

main()
