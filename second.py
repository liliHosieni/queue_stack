from tkinter import *
class node:

    def __init__(self, data) -> None:
        if(data):                           #for cyc that dont have data
            self.data = str(data)
        else:
            self.data = None
        self.link = None

class Clinked_list:

    def __init__(self, *tupple) -> None:        #make the simple list
        self.cyc = node(None)                   #The node is the beginning of the cycle
        self.List = list(tupple)                #Convert to list
        self.first = node(self.List[0])    
        self.List.pop(0)
        y = self.first                          #Save the last node

        for x in self.List:
            n = node(x)
            y.link = n
            y = n                               #Save the last node
    
    def make_cycle(self, x):                    #make cycle from x to the end
        x = str(x)
        p = self.first
        q = None
        while(p != None):
            if(p.data == x):
                self.cyc = p                    #The node We are going to get back to it
            q = p
            p = p.link
        q.link = self.cyc                       #End of node

    def have_Cycle(self):
        p = self.first
        while(p):
            if(p.data.find("+") != -1):
                print("Have cycle")
                return
            p.data = p.data + "+"
            p = p.link
        print("No cycle")

    def List_Print(self):
        p = self.first
        if(self.cyc.data):                          #when list have a cycle
            while(p != self.cyc):                   #print until cycle
                print(p.data, end=" ")
                p = p.link 
            print(p.data, end=" ")                  #print first node of cycle
            p = p.link
            while(p != self.cyc):                   #print Continuation of the node
                print(p.data, end=" ")
                p = p.link
            print()
        else:
            while(p):
                print(p.data, end=" ")              #when list dont have a cycle
                p = p.link
            print()


#-------------------------------------------------------------------------------------Example:
#|input
c = Clinked_list(3, 4, 5, 6, 7, 8, 9)              
c.make_cycle(6)                                     
#|output
c.List_Print()
c.have_Cycle()








