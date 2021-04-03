import tkinter as tk 
window = tk.Tk()

previousInputStr = str()

def addText(input):
    inputField.insert(len(inputField.get()),input)


previousInput = tk.Label(text=previousInputStr)
inputField = tk.Entry(justify="right",width=36,size=15)
button = tk.Button(text="click",command=addText)

previousInput.grid(row=0,column=0)
inputField.grid(row=1,column=0,columnspan=3)


buttonHeight=3
buttonWidth=9
siffrorX=2
siffrorY=0

bEquals = b0 = tk.Button(text = "=",height=buttonHeight,width=buttonWidth)
b0 = tk.Button(text = "0",height=buttonHeight,width=buttonWidth)
b1 = tk.Button(text = "1",height=buttonHeight,width=buttonWidth)
b2 = tk.Button(text = "2",height=buttonHeight,width=buttonWidth)
b3 = tk.Button(text = "3",height=buttonHeight,width=buttonWidth)
b4 = tk.Button(text = "4",height=buttonHeight,width=buttonWidth)
b5 = tk.Button(text = "5",height=buttonHeight,width=buttonWidth)
b6 = tk.Button(text = "6",height=buttonHeight,width=buttonWidth)
b7 = tk.Button(text = "7",height=buttonHeight,width=buttonWidth)
b8 = tk.Button(text = "8",height=buttonHeight,width=buttonWidth)
b9 = tk.Button(text = "9",height=buttonHeight,width=buttonWidth)
b1.grid(row=siffrorX, column=siffrorY)
b2.grid(row=siffrorX, column=siffrorY+1)
b3.grid(row=siffrorX, column=siffrorY+2)
b4.grid(row=siffrorX+1, column=siffrorY)
b5.grid(row=siffrorX+1, column=siffrorY+1)
b6.grid(row=siffrorX+1, column=siffrorY+2)
b7.grid(row=siffrorX+2, column=siffrorY)
b8.grid(row=siffrorX+2, column=siffrorY+1)
b9.grid(row=siffrorX+2, column=siffrorY+2)
b0.grid(row=siffrorX+3,column=siffrorY+1)
bEquals.grid(row=siffrorX+3,column=siffrorY+2)

window.mainloop()

# while ((there is an operator at the top of the operator stack)
#               and ((the operator at the top of the operator stack has greater precedence)
#                   or (the operator at the top of the operator stack has equal precedence and the token is left associative))
#               and (the operator at the top of the operator stack is not a left parenthesis)):