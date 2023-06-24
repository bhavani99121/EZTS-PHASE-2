stack=[]
def push():
    ele=int(input("enter element:"))
    stack.append(ele)
    print("\nelement inserted successfully\n")
def pop():
    if not stack:
        print("\nstack is empty\n")
    else:
        e=stack.pop()
        print("\nelement removed successfully\n")
def display():
    print(stack)
def top():
    if not stack:
        print("\nstack is empty\n")
    else:
        print("\ntop element is:",stack[-1])
while(1):
    ch=int(input("enter your choice:\n1-push\n2-pop\n3-display\n4-peek\n5-quit"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        top()
    elif ch==5:
        break
    else:
        print("\nplease enter valid option!\n")
        
