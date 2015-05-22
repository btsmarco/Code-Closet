# Jim and the Skyscrapers
# hackerrank.com
# Marco Botros

# Perfromance analysis: O(n*2)

N = int(input())
skyscpStr = input()

skyscp = skyscpStr.split()
skyscp = list(map(int,skyscp))

def CalculateRoutes(skList):

    possibleRoute = -1      # True if positive and equal to
                            # index as num, False if -1
    routes = 0
    c = 0
    while c < len(skList):
        elem = skList[c]
        k = c + 1
        while k < len(skList):
            skysHieght = skList[k]

            if elem >= skysHieght:
               possibleRoute = k
            if elem == skysHieght:
               if possibleRoute != -1 or (k == c+1):
                   routes += 1
            elif elem < skysHieght:
               possibleRoute = -1
               break

            k += 1

        c += 1

    return routes*2


result = CalculateRoutes(skyscp)
print(result)

# Test cases
# 7
# 5 5 5 5 5 5 5
# (42)
#
# 7
# 5 6 2 3 7 7 7
# (6)
#
# 4
# 3 2 4 3
# (0)
#
# 3
# 1 1000 1
# (0)
#
# 6
# 3 2 1 2 3 3
# (8)
#
# 3
# 5 5 5
# (6)
