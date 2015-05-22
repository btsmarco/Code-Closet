# Draft.py
# Marco Botros

import sys
TheList = ["fifth", "fourth", "thrid", "second", "first"]

TheSecondList = [-1, -2, 4, 4, 5, 3, 0, -2, 6, 8]

for i,v in enumerate(TheSecondList):
    if (v <= 0 ):
        TheSecondList.pop(i)

print(TheSecondList)

TheSecondList = [-1, -2, 4, 4, 5, 3, 0, -2, 6, 8]
count = 0
for i in TheSecondList[:]:
    if (i > 0 ):
        TheSecondList.append(i)
    count += 1
print(count)
print(TheSecondList)
print(len(TheSecondList))

def func(name):
    print("Got you Mr.",name)

func(sys.argv[1])
