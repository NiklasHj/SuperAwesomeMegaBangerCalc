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
    convertedInput.append(temp)
    return convertedInput

def fixFunctions(input):
    for x in range(len(input)):
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
    return input

def fixOperators(input):
    for x in range(len(input)):
        if input[x] == "^":
            input[x] = "**"
        if input[x] == "π":
            input[x] = "math.pi()"

print(convertInput("sin34*2/5"))
print(fixFunctions(convertInput("sin34*2/5")))
print(eval("".join(fixFunctions(convertInput("sin34*2/5")))))
print(math.pi,math.e)