#perform a function to check if binary tree is balanced left nodes smaller than right vice versa and diff height is 1max
def is_balanced(node):
    if node is None:
        return True,0
    balanced_l,height_l=is_balanced(node.left)
    balanced_r,height_r=is_balanced(node.right)
    balanced=balanced_l and balanced_r and abs(height_1-height_r)<=1
    height=1+max(height_l,height_r)
 
#create a balanced binary search tree given a sorted array.Start in the middle out binary search method   
def make_balanced_bst(data,lo=0,hi=None,parent=None):
    if hi is None:
        hi=len(data)-1
    if lo>=hi:
        return None #empty subtree
    mid=(lo+hi)//2
    key,value=data[mid]#username and userobject
    
    root=BSTNode(key,value)
    root.parent=parent
    root.left=make_balanced_bst(data,lo,mid-1,root)
    root.right=make_balanced_bst(data,mid+1,hi,root)
    return root
def list_all(node):
        if node is None:
            return []
        return list_all(node.left)+[(node.key,node.value)]+list_all(node.right)

#making an unbalanced or unskewed bst balanced
def balance_bst(node):
    return make_balanced_bst(list_all(node))