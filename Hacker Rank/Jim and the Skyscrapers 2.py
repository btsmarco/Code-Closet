# Jim and the Skyscrapers, algo 2
# hackerrank.com
# Marco Botros

# Performance analysis: O(n)
#     list.append() - O(1)
#     'in' dict - O(1)
#     for loop - O(n)

# Wrong answer - does not pass all test cases

N = int(input())
skyscpStr = input()

skyscp = skyscpStr.split()
skyscp = list(map(int,skyscp))

def CalculateRoutes(skList):

    routeStack = [skList[0]]

    valuesInStack = {}
    valuesInStack[skList[0]] = 1
    routes = 0

    lastElem = skList[0]
    for i in skList[1:]:

        # if skyscraper is shorter than last elem
        if i < lastElem:
            routeStack.append(i)
            if i in valuesInStack:
                valuesInStack[i] += 1
            else:
                valuesInStack[i] = 1

        # if skyscraper is equal to the last elem
        if i == lastElem:
            routes += 1 * (valuesInStack[i])
            routeStack.append(i)
            valuesInStack[i] += 1

        # if skyscraper is taller than last elem
        if i > lastElem:
            if i in valuesInStack:
                routes += 1  * (valuesInStack[i])
                routeStack.append(i)
                valuesInStack[i] += 1
            else:
                if i > max(routeStack):
                    # if i is a new value and not in the dict
                    routeStack.clear()
                    valuesInStack = {}

                    routeStack.append(i)
                    valuesInStack[i] = 1
                else:
                    routeStack.append(i)
                    valuesInStack[i] = 1

        prev = lastElem
        lastElem = i


    return routes*2


result = CalculateRoutes(skyscp)
print(result)

# Test cases
#
# 9
# 1 2 5 9 10 6 8 8 10
#
# 6
# 3 2 1 2 3 3
#
# 7
# 5 5 5 5 5 5 5
#
# 9
# 1 2 3 4 5 4 6 5 1
#
# 11
# 4 3 2 1 4 5 2 1 2 3 5
#
# 6
# 3 2 5 5 6 5 5 1
#
# 3
# 1 1000 1
#
# 4
# 3 2 4 3
#
# 7
# 5 6 2 3 7 7 7
#
# 3
# 5 5 5
