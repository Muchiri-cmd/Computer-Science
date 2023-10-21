class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
tree=parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))
def tree_to_tuple(node):
    while node:
        if node is None:
            return None
    
        left_tuple = tree_to_tuple(node.left)
        right_tuple = tree_to_tuple(node.right)
    
    return (left_tuple, node.key, right_tuple)
tree_tuple = tree_to_tuple(tree)
print(tree_tuple)