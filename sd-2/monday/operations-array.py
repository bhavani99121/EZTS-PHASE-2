n=int(input("enter size of the array:"))
li=[]
for i in range(n):
    nums=int(input())
    li.append(nums)
print("enter 1-insert\n2-delete\n3-search\n4-sort\n5-display\n6-exit")
while(1):
    num=int(input("enter your choice:"))
    if num==1:
        li=[]
        for i in range(n):
            li.append(i)
        print(li)
    elif num==2:
        v=int(input("enter the element to delete:"))
        if v in li:
            li.remove(v)
        else:
            print("element not found")
    
    elif num==3:
        s=int(input("enter element to search:"))
        for i in li:
            if i==s:
               print("element found at location:",s)
            else:
               print("element not found")
   
    elif num==4:
        for i in li:
            for j in li:
                if j>j+1:
                    temp=j
                    j=j+1
                    j=temp
                    print(li)
    
    elif num==5:
      print(li)
    elif num==6:
       exit()
    else:
       print("invalid")

    
