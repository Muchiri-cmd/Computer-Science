class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class TreeMap:
    def __init__(self):
        self.root = None
    
    def __setitem__(self, key, value):
        node = self.find(self.root, key)
        if not node:
            self.root = self.insert(self.root, key, value)
            self.root = self.balance_bst(self.root)
        else:
            node.value = value
    
    def __getitem__(self, key):
        node = self.find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return iter(self.list_all(self.root))
    
    def __len__(self):
        return self.tree_size(self.root)
    
    def display(self):
        self.display_keys(self.root)
    
    @staticmethod
    def find(node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return TreeMap.find(node.left, key)
        if key > node.key:
            return TreeMap.find(node.right, key)
    
    @staticmethod
    def insert(node, key, value):
        if node is None:
            return BSTNode(key, value)
        if key < node.key:
            node.left = TreeMap.insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = TreeMap.insert(node.right, key, value)
            node.right.parent = node
        return node
    
    @staticmethod
    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        key, value = data[mid]
        root = BSTNode(key, value)
        root.parent = parent
        root.left = TreeMap.make_balanced_bst(data, lo, mid - 1, root)
        root.right = TreeMap.make_balanced_bst(data, mid + 1, hi, root)
        return root
    
    @staticmethod
    def balance_bst(node):
        data = TreeMap.list_all(node)
        return TreeMap.make_balanced_bst(data)
    
    @staticmethod
    def list_all(node):
        if node is None:
            return []
        return (
            TreeMap.list_all(node.left)
            + [(node.key, node.value)]
            + TreeMap.list_all(node.right)
        )
    
    @staticmethod
    def tree_size(node):
        if node is None:
            return 0
        return (
            TreeMap.tree_size(node.left)
            + 1
            + TreeMap.tree_size(node.right)
        )
    
    def display_keys(self, node=None, space='\t', level=0):
        if node is None:
            node = self.root

        if node is None:
            print(space * level + 'o')
            return

        if node.left is None and node.right is None:
            print(space * level + str(node.key))
            return

        self.display_keys(node.right, space, level + 1)
        print(space * level + str(node.key))
        self.display_keys(node.left, space, level + 1)

    def get_user_info(self, username):
        node = self.find(self.root, username)
        if node:
            return f"User(username='{node.value.username}', name='{node.value.name}', email='{node.value.email}')"
        return None



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

for key,value in treemap:
     print(key, treemap.get_user_info(key))