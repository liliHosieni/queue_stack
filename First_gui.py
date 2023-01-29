from tkinter import *
class node:                                         #Make node

    def __init__(self, data) -> None:
        self.data = data
        self.link = None

class Dlinked_list:

    def __init__(self) -> None:                         #list with extantion node
        empty_node = node(None)
        self.first = empty_node
        empty_node.link = self.first
    

ls = Dlinked_list()

def add_end():
    x = lb1.get()
    p = node(x)
    q = ls.first.link
    while(q.link != ls.first):                    #end of the list
        q = q.link
    q.link = p
    p.link = ls.first
    List_Print()

def add_first():
    x = lb2.get()
    p = node(x)
    p.link = ls.first.link
    ls.first.link = p
    List_Print()

def List_Print():                               #list print
    x = []
    p = ls.first.link
    while(p != ls.first):
        x.append(p.data)
        p = p.link
    lb3.configure(text= x)
    
def size():                                     #Number of node + extantion node
        p = ls.first.link
        x = 0
        while(p != ls.first):
            x += 1
            p = p.link
        lb5.configure(text= x+1)  

def empty():                                    #If list is empty, return true
    if(ls.first.link == ls.first ):             #Comparsion of first and first.link 
        lb6.configure(text="Yes")
    else:
        lb6.configure(text="No")

def swap():                                     #The values are swap
    i = lb7_i.get()
    j = lb7_j.get()
    p = ls.first.link
    while(p != ls.first):
        if(p.data == i):
            p.data = j
        elif(p.data == j):
            p.data = i
        p = p.link 
    List_Print() 

def removeX():                               #Remove all x in list
    x = lb8.get()
    q = ls.first
    p = q.link
    while(p != ls.first):
        if(p.data == x):
            q.link = p.link
        else:
            q = p
        p = p.link
    List_Print()

def List_Reverse_Print():                    #Reverse printing   
    x = []                                   #list member
    y = []                                   #reverse list member
    p = ls.first.link
    while(p != ls.first):
        x.append(p.data)
        p = p.link
    i = len(x) - 1
    while(i != -1):
        y.append(x[i])
        i = i - 1
    lb4.configure(text= y)                  #print


win1 = Tk()                                             #window
win1.minsize(600,460)
win1.title("ClinkedList")
win1.configure(background= "blueviolet")

Label(win1, height = 2, background = "blueviolet", text = "C Liked Lidt", font=("tahoma, 18")).pack()

m1 = PanedWindow(win1, background= "blueviolet")        #add end
m1.pack()
btn1 = Button(win1, text="ADD_END", command=add_end, background= "yellow")
lb1 = Entry(win1, background= "yellow")
m1.add(btn1)
m1.add(lb1)

Label(win1, height=1, background= "blueviolet").pack()

m2 = PanedWindow(win1, background= "blueviolet")        #add first
m2.pack()
btn2 = Button(win1, text="ADD_FIRST", command= add_first, background= "yellow")
lb2 = Entry(win1, background= "yellow")
m2.add(btn2)
m2.add(lb2)

Label(win1, height=1, background= "blueviolet").pack()

m3 = PanedWindow(win1, background= "blueviolet")        #print
m3.pack()
btn3 = Button(win1, text="PRINT", command=List_Print, background= "yellow")
lb3 = Label(win1, width=20, background= "yellow")
m3.add(btn3)
m3.add(lb3)

Label(win1, height=1, background= "blueviolet").pack()

m4 = PanedWindow(win1, background= "blueviolet")        #print reverse
m4.pack()
btn4 = Button(win1, text="PRINT_REVERSE", command=List_Reverse_Print, background= "yellow")
lb4 = Label(win1, width=20, background= "yellow")
m4.add(btn4)
m4.add(lb4)

Label(win1, height=1, background= "blueviolet").pack()

m5 = PanedWindow(win1, background= "blueviolet")        #size
m5.pack()
lb5 = Label(win1, width=20, background= "yellow")
btn5 = Button(win1, text="SIZE", command=size, background= "yellow")
m5.add(btn5)
m5.add(lb5)

Label(win1, height=1, background= "blueviolet").pack()

m6 = PanedWindow(win1, background= "blueviolet")        #empty
m6.pack()
lb6 = Label(win1, width=20, background= "yellow")
btn6 = Button(win1, text="EMPTY", command=empty, background= "yellow")
m6.add(btn6)
m6.add(lb6)

Label(win1, height=1, background= "blueviolet").pack()

m7 = PanedWindow(win1, background= "blueviolet")        #swap
m7.pack()
lb7_i = Entry(win1, width=11, background= "yellow")
lb7_j = Entry(win1, width=11, background= "yellow")
btn7 = Button(win1, text="swap", command=swap, background= "yellow")
m7.add(btn7)
m7.add(lb7_i)
m7.add(lb7_j)

Label(win1, height=1, background= "blueviolet").pack()

m8 = PanedWindow(win1, background= "blueviolet")        #delet x
m8.pack()
lb8 = Entry(win1, background= "yellow")
btn8 = Button(win1, text="DELETEX", command= removeX, background= "yellow")
m8.add(btn8)
m8.add(lb8)



win1.mainloop()                                         #loop