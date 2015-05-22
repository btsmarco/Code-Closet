# Swap Nodes
# hackerrank.com
# Marco Botros

class BinaryTree:
    def __init__(self,v):
        self.rootValue = v
        self.right = None
        self.left = None

    def getRootValue(self):
        return self.rootValue

    def setRootValue(self,v):
        self.rootValue = v

    def getRight(self):
        return self.right

    # Takes in a tree or basic types(int,str..etc)
    def setRight(self,r):
        if self.right:
            if type(r) != BinaryTree:
                (self.right).setRootValue(r)
            else:
                self.right = r
        else:
            if type(r) != BinaryTree:
                rTree = BinaryTree(r)
                self.right = rTree
            else:
                self.right = r

    def getLeft(self):
        return self.left

    def setLeft(self,L):
        if self.left:
            if type(L) != BinaryTree:
                (self.left).setRootValue(L)
            else:
                self.left = L
        else:
            if type(L) != BinaryTree:
                LTree = BinaryTree(L)
                self.left = LTree
            else:
                self.left = L

def inorder(tree,level):
    if tree:
        level += 1
        inorder(tree.getLeft(),level)
        print(tree.getRootValue(), level)
        inorder(tree.getRight(),level)

# _____________________________________
N = int(input())


# _____________________________________
Root = BinaryTree(5)

rT = BinaryTree(20)
rT.setRight(10)
Root.setRight(rT)

LT = BinaryTree(50)
LT.setLeft(3)
LT.setRight(2)
Root.setLeft(LT)

preorder(Root)
print()
Lev = 0
inorder(Root, Lev)
print()
