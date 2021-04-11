import tkinter as tk 
import fixInput
import math

window = tk.Tk()

previousInputStr = str()

def addText(input):
    inputField.insert(len(inputField.get()),input)

def clearInputField():
    inputField.delete(0,len(inputField.get()))

def pressEquals():
    s = inputField.get()
    addText("=")
    previousInputStr = inputField.get()
    clearInputField()
    previousInput = tk.Label(bg="light blue",text=previousInputStr,justify="right",width=51)
    previousInput.grid(row=0,column=0,columnspan=5)
    try:
        inputField.insert(0,eval("".join(fixInput.calculate(s))))
    except:
        inputField.insert(0,"Syntax error")

previousInput = tk.Label(bg="light blue",text=previousInputStr,justify="right",width=51)
inputField = tk.Entry(justify="right",width=32,font=("TkDefaultFont",15))
button = tk.Button(text="click",command=addText)

previousInput.grid(row=0,column=0,columnspan=5)
inputField.grid(row=1,column=0,columnspan=5)


buttonHeight=2
buttonWidth=9
siffrorY=4
siffrorX=1
operatorY=siffrorY+3 #Högra bottenhörnet börjar den på.
operatorX=siffrorX+3

bEquals = b0 = tk.Button(text = "=",height=buttonHeight,width=buttonWidth,bg="light green",command=pressEquals)
bPoint = b0 = tk.Button(text = ".",height=buttonHeight,width=buttonWidth,command=lambda: addText("."))
b0 = tk.Button(text = "0",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("0"))
b1 = tk.Button(text = "1",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("1"))
b2 = tk.Button(text = "2",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("2"))
b3 = tk.Button(text = "3",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("3"))
b4 = tk.Button(text = "4",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("4"))
b5 = tk.Button(text = "5",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("5"))
b6 = tk.Button(text = "6",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("6"))
b7 = tk.Button(text = "7",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("7"))
b8 = tk.Button(text = "8",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("8"))
b9 = tk.Button(text = "9",height=buttonHeight,width=buttonWidth,bg="white",command=lambda: addText("9"))
b1.grid(row=siffrorY+2, column=siffrorX)
b2.grid(row=siffrorY+2, column=siffrorX+1)
b3.grid(row=siffrorY+2, column=siffrorX+2)
b4.grid(row=siffrorY+1, column=siffrorX)
b5.grid(row=siffrorY+1, column=siffrorX+1)
b6.grid(row=siffrorY+1, column=siffrorX+2)
b7.grid(row=siffrorY, column=siffrorX)
b8.grid(row=siffrorY, column=siffrorX+1)
b9.grid(row=siffrorY, column=siffrorX+2)
bPoint.grid(row=siffrorY+3,column=siffrorX+1)
b0.grid(row=siffrorY+3,column=siffrorX)
bEquals.grid(row=siffrorY+3,column=siffrorX+2)


bPlus = tk.Button(text = "+",height=buttonHeight,width=buttonWidth,command=lambda: addText("+"))
bMinus = tk.Button(text = "-",height=buttonHeight,width=buttonWidth,command=lambda: addText("-"))
bMultiply = tk.Button(text = "*",height=buttonHeight,width=buttonWidth,command=lambda: addText("*"))
bDivision = tk.Button(text = "/",height=buttonHeight,width=buttonWidth,command=lambda: addText("/"))
bRaised = tk.Button(text = "^",height=buttonHeight,width=buttonWidth,command=lambda: addText("^"))
bClear = tk.Button(text = "CLEAR",height=buttonHeight,width=2*buttonWidth+1,command=clearInputField)
bLeftParent = tk.Button(text = "(",height=buttonHeight,width=buttonWidth,command=lambda: addText("("))
bRightParent = tk.Button(text = ")",height=buttonHeight,width=buttonWidth,command=lambda: addText(")"))

bSin = tk.Button(text = "sin",height=buttonHeight,width=buttonWidth,command=lambda: addText("sin"))
bCos = tk.Button(text = "cos",height=buttonHeight,width=buttonWidth,command=lambda: addText("cos"))
bTan = tk.Button(text = "tan",height=buttonHeight,width=buttonWidth,command=lambda: addText("tan"))
bLn = tk.Button(text = "ln",height=buttonHeight,width=buttonWidth,command=lambda: addText("ln"))
bLog = tk.Button(text = "log",height=buttonHeight,width=buttonWidth,command=lambda: addText("log"))

bRoot = tk.Button(text = "√",height=buttonHeight,width=buttonWidth,command=lambda: addText("√"))
bPi = tk.Button(text = "π",height=buttonHeight,width=buttonWidth,command=lambda: addText("π"))
bE = tk.Button(text = "e",height=buttonHeight,width=buttonWidth,command=lambda: addText("e"))

bPlus.grid(row=operatorY, column=operatorX)
bMinus.grid(row=operatorY-1, column=operatorX)
bMultiply.grid(row=operatorY-2, column=operatorX)
bDivision.grid(row=operatorY-3, column=operatorX)
bRaised.grid(row=operatorY-4, column=operatorX-1)
bLeftParent.grid(row=operatorY-4, column=operatorX-3)
bRightParent.grid(row=operatorY-4, column=operatorX-2)
bClear.grid(row=operatorY-5, column=operatorX-1,columnspan=2)


bSin.grid(row=operatorY-4, column=operatorX-4)
bCos.grid(row=operatorY-3, column=operatorX-4)
bTan.grid(row=operatorY-2, column=operatorX-4)
bLn.grid(row=operatorY-1, column=operatorX-4)
bLog.grid(row=operatorY, column=operatorX-4)

bRoot.grid(row=operatorY-4, column=operatorX)
bPi.grid(row=operatorY-5, column=operatorX-3)
bE.grid(row=operatorY-5, column=operatorX-2)

bGraph = tk.Button(text = "Graph",height=buttonHeight,width=buttonWidth,bg="yellow")

bGraph.grid(row=operatorY-5, column=operatorX-4,)
window.mainloop()
# while ((there is an operator at the top of the operator stack)
#               and ((the operator at the top of the operator stack has greater precedence)
#                   or (the operator at the top of the operator stack has equal precedence and the token is left associative))
#               and (the operator at the top of the operator stack is not a left parenthesis)):