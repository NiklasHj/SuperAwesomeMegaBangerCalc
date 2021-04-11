import math


def convertInput(rawInput):
    rawInput = rawInput.replace(" ","")
    temp = ""
    convertedInput = []
    for x in rawInput:
        if x in "0123456789":
            temp += x
            continue
        else:
            if temp != "":
                convertedInput.append(temp)
                temp = ""
            convertedInput.append(x)
    if temp != "":
        convertedInput.append(temp)
    return convertedInput

def fixFunctions(input):
    print(input)
    print(len(input))
    x = -1
    for token in input:
        x += 1
        print(input[x])
        if input[x] == "s":
            input.pop(x+1)
            input.pop(x+1)
            input[x] = "math.sin"
            if input[x+1] != "(":
                input.insert(x+1,"(")
                input.insert(x+3,")")
        if input[x] == "c":
            input.pop(x+1)
            input.pop(x+1)
            input[x] = "math.cos"
            if input[x+1] != "(":
                input.insert(x+1,"(")
                input.insert(x+3,")")
        if input[x] == "t":
            input.pop(x+1)
            input.pop(x+1)
            input[x] = "math.tan"
            if input[x+1] != "(":
                input.insert(x+1,"(")
                input.insert(x+3,")")
        if input[x] == "l" and input[x+1] == "n":
            input.pop(x+1)
            input[x] = "math.log"
            if input[x+1] != "(":
                input.insert(x+1,"(")
                input.insert(x+3,")")
        if input[x] == "l" and input[x+1] == "o":
            input.pop(x+1)
            input.pop(x+1)
            input[x] = "math.log10"
            if input[x+1] != "(":
                input.insert(x+1,"(")
                input.insert(x+3,")")      
    return input
math.factorial
def fixOperators(input):
    for x in range(len(input)):
        if input[x] == "^":
            input[x] = "**"
        if input[x] == "√":
            input[x] = "math.sqrt"
            if input[x+1] != "(":
                input.insert(x+1,"(")
                input.insert(x+3,")")
        if input[x] == "π":
            input[x] = "math.pi"
        if input[x] == "e":
            input[x] = "math.e"
    return input

def calculate(input):
    return fixOperators(fixFunctions(convertInput(input)))
print(len(["","","","","","","",""]))
print(convertInput("log(25*4)"))
print(fixFunctions(convertInput("log(25*4)")))
# print(eval("".join(fixFunctions(convertInput("log(25*4")))))
