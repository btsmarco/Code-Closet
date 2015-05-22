# Testing Bigger is Greater2.py
# Marco Botros

#from BiggerIsGreater import main

#main()

MyOutput = open("Out.txt","r")
RightOutput = open("output01.txt","r")
TheInput = open("input01.txt",'r')

T = int(TheInput.readline())

for i in range(T):
    myLine = MyOutput.readline()
    rightLine = RightOutput.readline()
    inputLine = TheInput.readline()
    if (myLine != rightLine):
        print(i)
        print(inputLine)
        print(myLine, rightLine)
        
