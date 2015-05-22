# Cut the sticks
# Hackerank.com
# Marco Botros

N = int(input())

IntArray = (input()).split()

SticksArray = list(map(int,IntArray))

TotalCutSticks = 0

# Cuts the sticks with the cut size given
# Input is cutsize (Num) and the List of sticks
# Output is the modified list of sticks
def CutSticks(Num,SticksList):
    for i in range(len(SticksList)):
        SticksList[i] -= Num
    return SticksList

while (len(SticksArray) != 0):
    # 1. sort
    SticksArray.sort()

    # 2. clear zeros
    # 3. find smallest

    while(SticksArray[0]==0):
        SticksArray.remove(0)
        if len(SticksArray) == 0:
            break

    if len(SticksArray) == 0:
        break

    CutSize = SticksArray[0]

    # 4. Cut
    SticksArray = CutSticks(CutSize,SticksArray)

    # 5. Count cut sticks
    print(len(SticksArray))
