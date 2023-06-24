n=int(input("enter size of array:"))
li=[]
for i in range(n):
    nums=int(input())
    li.append(nums)
print("enter 1-insert\n2-delete\n3-search\n4-sort\n5-display\n6-exit")
while(1):
    ch=int(input("enter choice:"))
    if ch==1:
        n1=int(input("enter value:"))
        li.append(n1)
        print(li)
    elif ch==2:
        n2=int(input("enter element to delete:"))
        for i in li:
            if n2==i:
                li.remove(n2)
                print("element deleted successfully")
                break
            else:
                print("element not found")
                
    elif ch==3:
        n3=int(input("enter element to search:"))
        for i in li:
            if i==n3:
                print("element found")
            else:
                print("element not found")
    elif ch==4:
        for i in li:
            for j in li:
                if j>j+1:
                    temp=li[j]
                    li[j+1]=li[j]
                    li[j]=temp
        print(li)
    elif ch==5:
        print(li)
    elif ch==6:
        exit()
    else:
        print("invalid")
    

                    
                    
