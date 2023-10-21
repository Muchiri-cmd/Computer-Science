class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
    def __repr__(self):
      return "User(username='{}',name='{}',email={}')".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()  
class UserDatabase:
    def __init__(self):
        self.users=[]
    
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
       
    def find(node,key):
        if node is None:
            return None
        if key==node.key:
            return node
        if key<node.key:
            return UserDatabase.find(node.left,key)
        if key>node.key:
            return UserDatabase.find(node.right,key)
        else:
            return None
    
    def update(node,key,value):
        target=UserDatabase.find(node,key)
        if target is not None:
            target.value=value
    
    def list_all(node):
        if node is None:
            return []
        return UserDatabase.list_all(node.left)+[(node.key,node.value)]+UserDatabase.list_all(node.right)
    
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
    
        UserDatabase.display_keys(node.right,space,level+1)
        print(space*level+str(node.key))
        UserDatabase.display_keys(node.left,space,level+1)
#list of users for testcases
aakash=User('aakash','Aakash Rai','aakash@example.com')
biraj=User('biraj','Biraj Das','biraj@example.com')
hemanth=User('hemanth','Hemanth Jain','hemanth@example.com')
jadhesh=User('jadhesh','Jadhesh Verma','jadhesh@example.com')
siddhant=User('siddhant','Siddhant Sinha','siddhant@example.com')
sonaksh=User('sonaksh','Sonaksh Kumar','sonaksh@example.com')
vishal=User('vishal','Vishal Goel','vishal@example.com')
#users=[aakash,biraj,hemanth,jadhesh,siddhant,sonaksh,vishal]

class BSTNode():
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

#level0
#tree=BSTNode(jadhesh.username,jadhesh)
#print(tree.key,tree.value)

#level1
#tree.left=BSTNode(biraj.username,biraj)
#tree.right=BSTNode(sonaksh.username,sonaksh)
#tree.right.parent=tree
#view level 1
#print(tree.left.key,tree.left.value,tree.right.key,tree.right.value)
        
tree=UserDatabase.insert(None,jadhesh.username,jadhesh)#as the first node where there was no node or nothing 
UserDatabase.insert(tree,biraj.username,biraj)
UserDatabase.insert(tree,sonaksh.username,sonaksh)
UserDatabase.insert(tree,aakash.username,aakash)
UserDatabase.insert(tree,hemanth.username,hemanth)
UserDatabase.insert(tree,siddhant.username,siddhant)
UserDatabase.insert(tree,vishal.username,vishal)
#print(UserDatabase.display_keys(tree))
#node=UserDatabase.find(tree,'Tanya')
#print(node)
#UserDatabase.update(tree,'hemanth',User('hemanth','Hemanth J',"hemanthj@example.com"))
#node=UserDatabase.find(tree,'hemanth')
#print(node.value)
full_tree=UserDatabase.list_all(tree)
print(full_tree)
















"""database=UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(biraj)
user=database.find('siddhant')
database.update(User(username='siddhant',name='Siddhant U',email='siddhantu@example.com'))

users=database.list_all()
print(users)"""

