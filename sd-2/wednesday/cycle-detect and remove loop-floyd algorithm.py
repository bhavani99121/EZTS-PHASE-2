class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def insert(self,n_data):
        n_data=node(n_data)
        n_data.next=self.head
        self.head=n_data
    def detect_and_remove_loop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        fp=self.head
        sp=self.head

        while(fp and sp and sp.next):
            fp=fp.next
            sp=sp.next.next

            if fp==sp:
                print("meeting point is:",fp.data)
                fp=self.head

                while (fp.next!=sp.next):
                    fp=fp.next
                    sp=sp.next
                print("start of loop=",sp.next.data)
                sp.next=None
    def display(self):
                     temp=self.head#temp assigned to first node
                     while temp:
                       print(temp.data,end=" ")
                       if temp.next!=None:
                          print("->",end=" ")
                       temp=temp.next
obj=ll()
obj.head=node(50)
obj.head.next=node(20)
obj.head.next.next=node(15)
obj.head.next.next.next=node(4)
obj.head.next.next.next.next=node(10)

extra=node(1)
obj.head.next.next.next.next.next=extra
extra.next=obj.head.next

obj.detect_and_remove_loop()
print("list after removing loop")
obj.display()

                    
        
