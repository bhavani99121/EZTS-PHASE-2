class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_next(self,data):
        if self.tail is None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail=self.tail.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            if temp.next!=None:
                print("->",end=" ")
            temp=temp.next
            
obj=sll()
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter data:"))
    obj.add_next(data)
obj.display()
    
