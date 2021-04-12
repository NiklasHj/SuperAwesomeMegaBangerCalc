rawInput = str(input("input = "))
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
print(convertedInput)
