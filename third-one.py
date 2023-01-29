from tkinter import *
class node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None


class LinkStack:
    def __init__(self) -> None:
        self.top = None
    
    def add(self, x):                       #add
        p = node(x)
        p.link = self.top
        self.top = p
    
    def delet(self):
        if(self.top):
            x = self.top.data
            self.top = self.top.link
            return x
        else:                               #for empty stack
            print("stack is empty")
            return None

    def print_lStack(self):
        p = self.top
        while(p != None):
            print(p.data, end=" ")
            p = p.link
        print()

    def empty(self):
        if(self.top == None):
            return True
        return False



def output():
    x = input.get()
    a = True
    stack = LinkStack()
    for i in range(len(x)):                 
        match(x[i]):
            case "{" | "(" | "[":               #( { [ add to stack
                stack.add(x[i])

            case "}":
                if(not stack.empty()):
                    if(stack.top.data == "{"):  #if {}, remove { from stack
                        stack.delet()
                else:
                    out.configure(text="Not balance")
                    a = False
                    break
            case ")":
                if(not stack.empty()):
                    if(stack.top.data == "("):  #if (), remove ( from stack
                        stack.delet()
                else:
                    out.configure(text="Not balance")
                    a = False
                    break
            case "]":
                if(not stack.empty()):
                    if(stack.top.data == "["):  #if [], remove [ from stack
                        stack.delet()
                else:
                    out.configure(text="Not balance")
                    a = False
                    break

    if(a):                                      #Checking that the stack is completely empty
        if(stack.empty()):
            out.configure(text="balance")
        else:
            out.configure(text="Not balance")


window = Tk()
window.configure(background="yellow")
window.title("second_project")
window.minsize(400,300)
Label(window, height=2, background="yellow", text="Checking", font=("tahoma, 18")).pack()
input = Entry(window, background= "black", fg="white") 
input.pack()
Label(window, height=1, width= 1, background="yellow").pack()
btn = Button(window,text= "Run" , command = output, background= "black", fg="white")
btn.pack()

Label(window, background="yellow", height=1).pack()
out = Label(window, background="yellow", fg="black",font=(18))
out.pack()


window.mainloop()




