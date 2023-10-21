def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left),tree_height(node.right))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left)+tree_size(node.right)
    

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

tree=parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))
print(tree_height(tree))
print(tree_size(tree))
