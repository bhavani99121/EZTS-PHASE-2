class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val,end=" ")
        printinorder(root.right)
def printpreorder(root):
    if root:
        print(root.val,end=" ")
        printpreorder(root.left)
        printpreorder(root.right)

def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val,end=" ")
n=node(100)
n.left=node(400)
n.right=node(500)
n.left.left=node(700)
n.left.right=node(600)
n.left.right.left=node(900)
n.right.left=node(800)
n.right.right=node(200)
n.right.right.left=node(300)
print("\npre-order traversal\n")
printpreorder(n)
print("\nin-order traversal\n")
printinorder(n)
print("\npost-order traversal\n")
printpostorder(n)



