class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert_at_pos(self,pos,data):
        nn=node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nn.next=temp.next
        temp.next=nn
    def display(self):
        if self.head is None:
            print('list is empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
obj=sll()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
obj.display()
print("")
obj.insert_at_pos(6,100)
obj.display()
        
        
