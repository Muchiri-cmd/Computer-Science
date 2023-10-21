#tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))

class Treenode:
    def __init__(self,key):
        self.key,self.left,self.right=key,None,None
        
    #helper function to convert tree back to tuple 
    def tree_to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return Treenode.tree_to_tuple(self.left),self.key,Treenode.tree_to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.tree_to_tuple())
    def __repr__(self):
        return  "BinaryTree <{}>".format(self.tree_to_tuple())  


        #helper function to display the keys for a binary tree for visualization
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
    
    def tree_height(node):
        if node is None:
            return 0
        return 1 + max(tree_height(node.left),tree_height(node.right))

    def tree_size(node):
        if node is None:
            return 0
        return 1 + tree_size(node.left)+tree_size(node.right)
    

    def inorder_traversal(node):
        if node is None:
            return[]
        return(inorder_traversal(node.left)+
        [node.key]+
        inorder_traversal(node.right)) #keeps adding the keys
    
    #helper function to construct a binary tree and its nodes
    @staticmethod
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



tree = Treenode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree.key)
print(tree.left.key,tree.right.key)
print(tree.left.left.key,tree.right.left.key,tree.right.right.key)
print(tree.right.left.right.key,tree.right.right.left.key)
print(tree)

Treenode.display_keys(tree,' ')
tuple_representation = Treenode.tree_to_tuple(tree)
print(tuple_representation)
    


