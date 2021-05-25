

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
    x = 0
    while x <= len(convertedInput)-1:
        if convertedInput[x] == "π":
            convertedInput[x] = "math.pi"
        elif convertedInput[x] == "e":
            convertedInput[x] = "math.e"
        elif convertedInput[x] == "s":
            convertedInput[x] = "sin"
            convertedInput.pop(x+1)
            convertedInput.pop(x+1)
        elif convertedInput[x] == "c":
            convertedInput[x] = "cos"
            convertedInput.pop(x+1)
            convertedInput.pop(x+1)
        elif convertedInput[x] == "t":
            convertedInput[x] = "tan"
            convertedInput.pop(x+1)
            convertedInput.pop(x+1)
        elif convertedInput[x] == "l" and convertedInput[x+1] == "o":
            convertedInput[x] = "log"
            convertedInput.pop(x+1)
            convertedInput.pop(x+1)
        elif convertedInput[x] == "l" and convertedInput[x+1] == "n":
            convertedInput[x] = "ln"
            convertedInput.pop(x+1)
        x += 1
    return convertedInput

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def shuntingYard(convertedInput):

    outputQue = []
    operatorStack = []
    precedence = 0
    associative = ""
    n = 0
    for token in convertedInput:
        if is_number(token) == True:
            outputQue.append(token)
        elif token in "+-*/^":
            if token in "+-":
                precedence = 2
                associative = "left"
            if token in "*/":
                precedence = 3
                associative = "left"
            if token in "^":
                precedence = 4
                associative = "right"
            while ((len(operatorStack) != 0) and ((operatorStack[-1][1] > precedence) or (operatorStack[-1][1] == precedence and associative == "left")) and (operatorStack[-1][0] != "(")):
                outputQue.append(operatorStack.pop(-1)[0])
            operatorStack.append([token,precedence,associative])
        elif token == "(":
            smallList = convertedInput.copy()
            for x in range(n+1):
                smallList.pop(0)
            outputQue.append(shuntingYard(smallList))
            # operatorStack.append([token,0,0])
        elif token == ")":
            convertedInput.pop(n)
            break
            # while operatorStack[-1][0] != "(":
            #     outputQue.append(operatorStack.pop(-1)[0])
            #     if len(operatorStack) == 0:
            #         return "Missmatched parentheses"
            # if operatorStack[-1][0] == "(":
            #     operatorStack.pop(-1)
        n += 1
    # if there is a function token at the top of the operator stack, then:
    # #             pop the function from the operator stack onto the output queue.
    if len(operatorStack) != 0:
        for n in range(len(operatorStack)):
            outputQue.append(operatorStack.pop(-1)[0])
        operatorStack = []
    return RPNCalculator(outputQue)

def RPNCalculator(tal):
    while len(tal) != 1:
        for x in range(len(tal)):
            if tal[x] in "+-*/^" and is_number(tal[x]) == False:
                print(tal)
                print(tal[x-2],tal[x-1])
                if tal[x] == "+":
                    tal[x] = str(float(tal[x-2]) + float(tal[x-1]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x] == "-":
                    tal[x] = str(float(tal[x-2]) - float(tal[x-1]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x] == "*":
                    tal[x] = str(float(tal[x-2]) * float(tal[x-1]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x] == "/":
                    tal[x] = str(float(tal[x-2]) / float(tal[x-1]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x] == "^":
                    tal[x] = str(float(tal[x-2]) ** float(tal[x-1]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                break
            elif tal[x] in "√":
                if tal[x] == "√":
                    tal[x] = str(float(tal[x-1]) ** 0.5)
                    tal.pop(x-1)
                break
    return tal[0]
# print(RPNCalculator(["3" ,"4" ,"2" ,"*","1", "5", "-", "2", "3", "^", "^", "/", "+"]))
print(shuntingYard(convertInput("30 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")))
# print(convertInput("30 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))

# while there are tokens to be read:
#     read a token.
#     if the token is a number, then:
#         push it to the output queue.
#     else if the token is a function then:
#         push it onto the operator stack 
#     else if the token is an operator then:
#         while ((there is an operator at the top of the operator stack)
#               and ((the operator at the top of the operator stack has greater precedence)
#                   or (the operator at the top of the operator stack has equal precedence and the token is left associative))
#               and (the operator at the top of the operator stack is not a left parenthesis)):
#             pop operators from the operator stack onto the output queue.
#         push it onto the operator stack.
#     else if the token is a left parenthesis (i.e. "("), then:
#         push it onto the operator stack.
#     else if the token is a right parenthesis (i.e. ")"), then:
#         while the operator at the top of the operator stack is not a left parenthesis:
#             pop the operator from the operator stack onto the output queue.
#         /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
#         if there is a left parenthesis at the top of the operator stack, then:
#             pop the operator from the operator stack and discard it
#         if there is a function token at the top of the operator stack, then:
#             pop the function from the operator stack onto the output queue.
# /* After while loop, if operator stack not null, pop everything to output queue */
# if there are no more tokens to read then:
#     while there are still operator tokens on the stack:
#         /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
#         pop the operator from the operator stack onto the output queue.
# exit.