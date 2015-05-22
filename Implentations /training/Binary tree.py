# Binary tree
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

def TraverseTree(Tree):

    currentTree = Tree
    parentTree = None
    visitedLeft = False
    counter = 0
    while counter < 6:
        if not visitedLeft:
            yield currentTree.getRootValue()

        if currentTree.getLeft() and not visitedLeft:
            parentTree = currentTree
            currentTree = currentTree.getLeft()
            visitedLeft = False
        elif (currentTree.getLeft() == None) and (currentTree.getRight() == None):
            currentTree = parentTree
            visitedLeft = True
        elif currentTree.getRight() and visitedLeft:
            parentTree = currentTree
            currentTree = currentTree.getRight()
            visitedLeft = False
        counter += 1

def PrintTree(Tree):
    node = Tree
    while node:
        print(node.getRootValue())
        print((node.getRight()).getRootValue())
        print((node.getLeft()).getRootValue())
        print()

        if node.getRight():
            node = node.getRight()
        elif node.getLeft():
            node = node.getLeft()
        else:
            node = None

def preorder(tree):
    if tree:
        print(tree.getRootValue(),end=" ")
        preorder(tree.getLeft())
        preorder(tree.getRight())

def inorder(tree,level):
    if tree:
        level += 1
        inorder(tree.getLeft(),level)
        print(tree.getRootValue(), level)
        inorder(tree.getRight(),level)

Root = BinaryTree(5)

rT = BinaryTree(20)
rT.setRight(10)
Root.setRight(rT)

LT = BinaryTree(50)
LT.setLeft(3)
LT.setRight(2)
Root.setLeft(LT)

# PrintTree(Root)
#for t in TraverseTree(Root):
#    print(t)

preorder(Root)
print()
Lev = 0
inorder(Root, Lev)
print()
