class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=node(data)
        else:
            nn=node(data)
            nn.next=self.head
            self.head=nn
    def pop(self):
        if self.head is None:
            print("\nstack is empty\n")
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
    def display(self):
        if self.head is None:
            print("\nstack is empty\n")
        else:
            temp=self.head#temp assigned to first node
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("<-",end=" ")
                temp=temp.next
    def top(self):
        if self.head is None:
            print("\nempty stack")
        else:
            print("top element is:",self.head.data)
obj=stack()
while(1):
    ch=int(input("\nenter your choice:\n1-push\n2-pop\n3-display\n4-peek\n5-quit"))
    if ch==1:
        n=int(input("enter value:"))
        obj.push(n)
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.display()
    elif ch==4:
        obj.top()
    elif ch==5:
        break
    else:
        print("\nplease enter valid option!\n")
            
        
        
