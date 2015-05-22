# Bigger is Greater
# hackerrank.com
# Marco Botros
from itertools import permutations

T = int(input())

# Applicable is not very well thought out
# Doesn't work all the time
def Applicable(seq):
    n = 2
    for i in range(len(seq)):
        result = GetLargestPerm(seq[:n])

        if (result == 'no answer'):
            if(abs(n) == len(seq)):
                print("first False")
                return(False)
            elif(n <= 6):
                n += 1
                continue
            else:
                print("second False")
                return(False)
        else:
            newSeq = result + seq[n:]

            if(newSeq > seq):
                return(True)
            else:
                n += 1
    print("third False")
    return(False)

def GetLargestPerm(seq):
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

    return resultStr

def main():

    for i in range(T):

        seq = input()

        #if not Applicable(seq):
        #    print('no answer because not applicable')
        #    continue

        n = -2
        for i in range(len(seq)):
            result = GetLargestPerm(seq[n:])

            if (result == 'no answer'):
                if(abs(n) == len(seq)):
                    newSeq = 'no answer'
                else:
                    n -= 1
                    continue
            else:
                newSeq = seq[:n] + result

                if(newSeq > seq):
                    break
                else:
                    n -= 1

        print(newSeq)

if __name__ == "__main__":
    main()
