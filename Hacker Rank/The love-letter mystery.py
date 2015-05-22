# The Love-Letter Mystery
# Hackerrank.com
# Marco Botros
from math import floor

T = int(input())

# Counts the least difference between 2 letters
def CalcOrd(tup):
    NumOfTurns = abs(ord(tup[0])- ord(tup[1]))
    return NumOfTurns

# Turn String to Palindrome
# input string
# outputs string
def CountToPalindrome(str):
    Length = len(str)
    odd = False
    if(Length%2 == 1): odd = True
    Center = floor(Length/2)
    TotalNum = 0
    
    # BeforeI = Center - X
    # AfterI = Center + X
    # X = range(0,Center)
    for x in range(0,Center):
        BeforeI = Center - x - 1    #The -1 to make it start from 0
        AfterI = Center + x
        if odd: AfterI += 1

        Intup = str[BeforeI], str[AfterI], 0
        #Pass in a tuple of 3 chars (letter1, letter2, numofturns)
        Num = CalcOrd(Intup)
        TotalNum += Num
    return TotalNum


for _ in range(T):
    InStr = input()
    Res = CountToPalindrome(InStr)
    print(Res)
