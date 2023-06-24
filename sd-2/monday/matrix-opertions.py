r=int(input("enter number of rows:"))
c=int(input("enter number of columns"))
li=[]
print("enter matrix elements:")
for i in range(r):
    li1=[]
    for j in range(c):
        
        li1.append(int(input()))
    li.append(li1)
print("enter matrix elements:\n")
for i in range(r):
    for j in range(c):
        print(li[i][j],end=" ")
    print()
print("\ndiagonal elements:\n")
for i in range(r):
    for j in range(c):
        if i==j:
            print(li[i][j],end=" ")
        else:
            print(" ",end=" ")
print("\nnon diagonal elements\n")
for i in range(r):
    for j in range(c):
        if i!=j:
            print(li[i][j],end=" ")
        else:
            print(" ",end=" ")
print("\nupper diagonal elements\n")
for i in range(r):
    for j in range(c):
        if i<j:
            print(li[i][j],end=" ")
        else:
            print(" ",end=" ")
print("\nlower diagonal elements\n")
for i in range(r):
    for j in range(c):
        if i>j:
            print(li[i][j],end=" ")
        else:
            print(" ",end=" ")

        
