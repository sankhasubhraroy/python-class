# Inner Function is a function defined inside another function

def isEven(num):
    isEvenBool = num % 2 == 0

    def printResult():
        if isEvenBool:
            print("Yes, The number is an even number")
        else:
            print("No, The number is not an even number")

    printResult()


isEven(57)
