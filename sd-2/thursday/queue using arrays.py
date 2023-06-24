queue=[]
def enqueue():
    ele=int(input("\nenter element:\n"))
    queue.append(ele)
    print(ele,"is added into queue\n")
def dequeue():
    if not queue:
        print("\nqueue is empty\n")
    else:
        e=queue.pop(0)
        print("\nremoved element",e)
def display():
    print(queue)
while(1):
    ch=int(input("enter your choice:\n1-enqueue\n2-dequeue\n3-display\n4-quit"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("\nplease enter valid option!\n")
