#creaing node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head#temp assigned to first node
            while temp.next!=self.head:
                if temp.next is None:
                    temp.next=self.head
                else:
                    print(temp.data,'->',end=' ')
                    temp=temp.next
            print(self.head.data)
                
obj=sll()
#node creation-initializing
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
obj.display()
