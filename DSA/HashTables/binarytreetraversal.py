"""def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)  # Traverse the left subtree
        print(node.key)  # Process the current node
        inorder_traversal(node.right)  # Traverse the right subtree
    #traverses until all left and right nodes have been traversed

def preorder_traversal(node):
    if node is not None:
        print(node.key)  # Process the current node
        preorder_traversal(node.left)  # Traverse the left subtree
        preorder_traversal(node.right)  # Traverse the right subtree

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)  # Traverse the left subtree
        postorder_traversal(node.right)  # Traverse the right subtree
        print(node.key)  # Process the current node
"""
class Treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None 
        

def parse_tuple(data):
    #print(data)
    if isinstance(data, tuple) and len(data)==3:
        node=Treenode(data[1])
        node.left=parse_tuple(data[0])
        node.right=parse_tuple(data[2])
    elif data is None:
        node=None
    else:
        node=Treenode(data)
    return node

def inorder_traversal(node):
    if node is None:
        return[]
    return(inorder_traversal(node.left)+
           [node.key]+
           inorder_traversal(node.right)) #keeps adding the keys

tree=parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))
ti=inorder_traversal(tree)
print(ti)