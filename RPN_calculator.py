def RPNCalculator(tal):
    while len(tal) != 1:
        for x in range(len(tal)):
            if tal[x][0] in "+-*/^":
                if tal[x][0] == "+":
                    tal[x] = str(float(tal[x-2][0]) + float(tal[x-1][0]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x][0] == "-":
                    tal[x] = str(float(tal[x-2][0]) - float(tal[x-1][0]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x][0] == "*":
                    tal[x] = str(float(tal[x-2][0]) * float(tal[x-1][0]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x][0] == "/":
                    tal[x] = str(float(tal[x-2][0]) / float(tal[x-1][0]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                elif tal[x][0] == "^":
                    tal[x] = str(float(tal[x-2][0]) ** float(tal[x-1][0]))
                    tal.pop(x-1)
                    tal.pop(x-2)
                break
            elif tal[x][0] in "√":
                if tal[x][0] == "√":
                    tal[x] = str(float(tal[x-1][0]) ** 0.5)
                    tal.pop(x-1)
                break
        print(tal)
    return tal

print(RPNCalculator(["3" ,"4" ,"2" ,"*","1", "5", "-", "2", "3", "^", "^", "/", "+"]))