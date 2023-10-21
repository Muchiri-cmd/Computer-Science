
class Treenode:
    def __init__(self,key):
        self.key,self.left,self.right=key,None,None
    def parse_tuple(data):
        #print(data)
        if isinstance(data, tuple) and len(data)==3:
            node=Treenode(data[1])
            node.left=Treenode.parse_tuple(data[0])
            node.right=Treenode.parse_tuple(data[2])
        elif data is None:
            node=None
        else:
            node=Treenode(data)
        return node

    def remove_nums(nums):
        return[x for x in nums if x is not None]
    def is_bst(node):
        if node is None:#considered a valid BST
            return True,None,None
    
        is_bst_l,min_l,max_l=Treenode.is_bst(node.left)
        is_bst_r,min_r,max_r=Treenode.is_bst(node.right)
    
        is_bst_node=(is_bst_l and is_bst_r and 
                 (max_l is None or node.key>max_l)and #condition1
                 (min_r is None or node.key<min_r))#condition2
        min_key=min(Treenode.remove_nums([min_l,node.key,min_r]))
        max_key=max(Treenode.remove_nums([max_l,node.key,max_r]))
    
        #print(node.key,min.key,max_key)
        return is_bst_node,min_key,max_key
    def display_keys(node,space='\t',level=0):
        #print(node.key if node else None,level)
    
        #if node is empty
        if node is None:
            print(space*level+'o')
            return
        #if node is a leaf
        if node.left is None and node.right is None:
            print(space*level + str(node.key))
            return
    
        Treenode.display_keys(node.right,space,level+1)
        print(space*level+str(node.key))
        Treenode.display_keys(node.left,space,level+1)


tree = Treenode.parse_tuple((('aakash','biraj', 'hemanth'), 'jadhesh', (('siddhant', 'sonaksh', 'vishal'))))
print(Treenode.is_bst(tree))
tree.display_keys()