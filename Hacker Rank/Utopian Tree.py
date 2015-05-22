T = int(input())

def SpringGC(h):
    return (h*2)

def SummerGC(h):
    return (h+1)

for _ in range(T):
    Height = 1  #meter
    N = int(input()) # number of cycles

    for i in range(1,N+1):
        if (i%2 != 0):
            Height = SpringGC(Height)
        elif (i%2 == 0):
            Height = SummerGC(Height)
    print (Height)
