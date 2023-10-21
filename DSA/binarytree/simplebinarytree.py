#implement a simple binary tree in python
class Treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None 
        
node0=Treenode(3)
node1=Treenode(4)
node2=Treenode(5)

node0.left=node1
node0.right=node2
tree=node0
print(tree.key)
print(tree.left.key)
print(tree.right.key)