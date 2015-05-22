# Bigger is Greater
# hackerrank.com
# Marco Botros
from itertools import permutations

T = int(input())

for i in range(T):

    seq = input()

    sortedPermSeq = sorted(list(set(permutations(seq))))

    result = ()
    for i,v in enumerate(sortedPermSeq):
        if (tuple(seq) == v):
            if(i == len(sortedPermSeq)-1):
                result = 'no answer'
            else:
                result = sortedPermSeq[i+1]
                break

        if (i == len(sortedPermSeq)-1):
            result = 'no answer'


    resultStr = ''.join(result)

    print(resultStr)
