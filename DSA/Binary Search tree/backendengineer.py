class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
        
class BSTNode():
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

class TreeMap():
    def __init__(self):
        self.root=None
    
    def __setitem__(self,key,value):
        node=TreeMap.find(self.root,key)
        if not node:
            self.root=TreeMap.insert(self.root,key,value)
            self.root=TreeMap.balance_bst(self.root)
        else:
            TreeMap.update(self.root,key,value)
            
    def __getitem(self,key):
        node=TreeMap.find(self.root,key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root)) #creates a generic iterable can be used within a for loop
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return TreeMap.display_keys(self.root)
    
    def find(node,key):
        if node is None:
            return None
        if key==node.key:
            return node
        if key<node.key:
            return TreeMap.find(node.left,key)
        if key>node.key:
            return TreeMap.find(node.right,key)
        else:
            return None
        
    def insert(node,key,value):
        if node is None:#empty subtree
            node=BSTNode(key,value)#insert or create a new node
        elif key<node.key:#examine key of node being inserted if less than node key ,inserted to left subtree
            node.left=UserDatabase.insert(node.left,key,value)#recursively adds to left node until an empty subtree
            node.left.parent=node#points to immediate node to keep track of things
        elif key>node.key:
            node.right=UserDatabase.insert(node.right,key,value)#''....
            node.right.parent=node#.....
        return node#returns original root...Ensures changes implemented correctly during the traversal
       
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
        
     #making an unbalanced or unskewed bst balanced
    def balance_bst(node):
        return TreeMap.make_balanced_bst(TreeMap.list_all(node))   
    
    def list_all(node):
        if node is None:
            return []
        return TreeMap.list_all(node.left)+[(node.key,node.value)]+TreeMap.list_all(node.right)
    
    def display_keys(node,space='\t',level=0):
        #print(node.key if node else None,level)
    
        #if node is empty
        if node is None:
            print(space*level+'o')
            return
        #if node is a leaf
        if node.root.left is None and node.root.right is None:
            print(space*level + str(node.key))
            return
    
        TreeMap.display_keys(node.right,space,level+1)
        print(space*level+str(node.key))
        Treemap.display_keys(node.left,space,level+1)
    
    def update(node,key,value):
        target=UserDatabase.find(node,key)
        if target is not None:
            target.value=value
     
aakash=User('aakash','Aakash Rai','aakash@example.com')
biraj=User('biraj','Biraj Das','biraj@example.com')
hemanth=User('hemanth','Hemanth Jain','hemanth@example.com')
jadhesh=User('jadhesh','Jadhesh Verma','jadhesh@example.com')
siddhant=User('siddhant','Siddhant Sinha','siddhant@example.com')
sonaksh=User('sonaksh','Sonaksh Kumar','sonaksh@example.com')
vishal=User('vishal','Vishal Goel','vishal@example.com')  

treemap=TreeMap()     
treemap['aakash']=aakash
treemap['jadhesh']=jadhesh
treemap['sonaksh']=sonaksh
print(treemap.root)
TreeMap.display_keys(treemap)