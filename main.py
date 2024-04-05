# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def decimalToNumeral(userInput): #converts a decimal number into roman numerals
    userInput = int(userInput)
    numeralValue = []

    while userInput - 1000 >= 0:
        numeralValue.append("M")
        userInput = userInput - 1000

    if userInput >= 900:
        numeralValue.append("C")
        numeralValue.append("M")
        userInput = userInput - 900

    while userInput - 500 >= 0:
        numeralValue.append("D")
        userInput = userInput - 500

    if userInput >= 400:
        numeralValue.append("C")
        numeralValue.append("D")
        userInput = userInput - 400

    while userInput - 100 >= 0:
        numeralValue.append("C")
        userInput = userInput - 100

    if userInput >= 90:
        numeralValue.append("X")
        numeralValue.append("C")
        userInput = userInput - 90

    while userInput - 50 >= 0:
        numeralValue.append("L")
        userInput = userInput - 50

    if userInput >= 40:
        numeralValue.append("X")
        numeralValue.append("L")
        userInput = userInput - 40

    while userInput - 10 >= 0:
        numeralValue.append("X")
        userInput = userInput - 10

    if userInput == 9:
        numeralValue.append("I")
        numeralValue.append("X")
        userInput = 0

    while userInput - 5 >= 0:
        numeralValue.append("V")
        userInput = userInput - 5

    if userInput == 4:
        numeralValue.append("I")
        numeralValue.append("V")
        userInput = 0

    while userInput - 1 >= 0:
        numeralValue.append("I")
        userInput = userInput - 1

    numeralValue = ''.join(numeralValue)
    print(numeralValue)

def numeralEntryErrorChecking(userInput, currentIndex): #basic error checking (looking for larger values after a given index)
    currentChar = userInput[currentIndex]
    if currentIndex < len(userInput) - 1:
        if currentChar == "I":
            if userInput[currentIndex + 1] == "L" or userInput[currentIndex + 1] == "C" or \
                userInput[currentIndex + 1] == "D" or userInput[currentIndex + 1] == "M":
                    print("invalid numeral")
                    return True
        elif currentChar == "V":
            if userInput[currentIndex + 1] == "L" or userInput[currentIndex + 1] == "C" or \
                userInput[currentIndex + 1] == "D" or userInput[currentIndex + 1] == "M" or \
                userInput[currentIndex + 1] == "X":
                    print("invalid numeral")
                    return True
        elif currentChar == "X":
            if userInput[currentIndex + 1] == "D" or userInput[currentIndex + 1] == "M":
                    print("invalid numeral")
                    return True
        elif currentChar == "L":
            if userInput[currentIndex + 1] == "L" or userInput[currentIndex + 1] == "C" or \
                userInput[currentIndex + 1] == "D" or userInput[currentIndex + 1] == "M":
                    print("invalid numeral")
                    return True
        elif currentChar == "D":
            if userInput[currentIndex + 1] == "M":
                print("invalid numeral")
                return True


def numeralToDecimal(userInput):
    decimalValue = 0 #final value printed
    numPasses = 0 #allows for skipping indices

    for index in range(len(userInput)):
        if numPasses > 0: #used to skip indices in the input string (in the case of IX, for example)
            numPasses = numPasses - 1
            continue

        if numeralEntryErrorChecking(userInput, index): #checks for invalid strings
            return

        if userInput[index] == "I":
             if index < len(userInput) - 1:
                if userInput[index + 1] == "V":
                    decimalValue = decimalValue + 4
                    numPasses = 1
                elif userInput[index + 1] == "X":
                    decimalValue = decimalValue + 9
                    numPasses = 1
                else:
                    decimalValue = decimalValue + 1
             else:
                 decimalValue = decimalValue + 1

        elif userInput[index] == "V":
            decimalValue = decimalValue + 5

        elif userInput[index] == "X":
            if index < len(userInput) - 1:
                if userInput[index + 1] == "L":
                    decimalValue = decimalValue + 40
                    numPasses = 1
                elif userInput[index + 1] == "C":
                    decimalValue = decimalValue + 90
                    numPasses = 1
                else:
                    decimalValue = decimalValue + 10
            else:
                decimalValue = decimalValue + 10

        elif userInput[index] == "L":
            decimalValue = decimalValue + 50

        elif userInput[index] == "C":
            if index < len(userInput) - 1:
                if userInput[index + 1] == "D":
                    decimalValue = decimalValue + 400
                    numPasses = 1
                elif userInput[index + 1] == "M":
                    decimalValue = decimalValue + 900
                    numPasses = 1
                else:
                    decimalValue = decimalValue + 100
            else:
                decimalValue = decimalValue + 100

        elif userInput[index] == "D":
            decimalValue = decimalValue + 500

        elif userInput[index] == "M":
            decimalValue = decimalValue + 1000

    print(decimalValue)

def romanNumeralConverter(): #main function
    userInput = ""

    print("Roman Numeral <--> Digit Converter")
    print("Type 'q' to quit!")

    while userInput != 'q':
        userInput = input("Enter either a roman numeral or a digit:")

        if userInput == 'q':
            return
        elif userInput.isnumeric():
            decimalToNumeral(userInput)
        else:
            numeralToDecimal(userInput)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    romanNumeralConverter()


