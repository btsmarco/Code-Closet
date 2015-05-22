# Angry Professor
# hackerrank.com
# Marco Botros

T = int(input())

def AreLate(TimeList,NumOfStudents):
    TimeList.sort()

    poped = 0
    for i in range(len(TimeList)):
        time = TimeList[i-poped]
        if time > 0:
            TimeList.pop(i-poped)
            poped += 1

    if NumOfStudents <= len(TimeList):
        return "NO"
    elif NumOfStudents > len(TimeList):
        return "YES"

# main function
def main(TestCases):
    for _ in range(TestCases):
        # Inputs
        Inputs = (input()).split()
        InputsList = list(map(int,Inputs))

        N = InputsList[0]
        K = InputsList[1]

        Students = (input()).split()
        StudentsList = list(map(int,Students))

        result = AreLate(StudentsList,K)

        print(result)
main(T)
