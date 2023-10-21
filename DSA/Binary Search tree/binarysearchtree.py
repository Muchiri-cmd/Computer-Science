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
    
    def insert(self,user):
        i=0 #pointer
        while i<len(self.users):#search space (as long as pointer is within db list)
            #find the first username greater than new username
            if self.users[i].username>user.username:#i=index of element
                break
            i+=1
        self.users.insert(i, user)#insert at that very index,the new username 
    
    def find(self,username):
        for user in self.users:
            if user.username==username:
                return user
    
    def update(self,user):
        target=self.find(user.username)
        target.name,target.email=user.name,user.email
    
    def list_all(self):
        return self.users
        
    
    
#list of users for testcases
aakash=User('aakash','Aakash Rai','aakash@example.com')
biraj=User('biraj','Biraj Das','biraj@example.com')
hemanth=User('hemanth','Hemanth Jain','hemanth@example.com')
jadhesh=User('jadhesh','Jadhesh Verma','jadhesh@example.com')
siddhant=User('siddhant','Siddhant Sinha','siddhant@example.com')
sonaksh=User('sonaksh','Sonaksh Kumar','sonaksh@example.com')
vishal=User('vishal','Vishal Goel','vishal@example.com')
#users=[aakash,biraj,hemanth,jadhesh,siddhant,sonaksh,vishal]


database=UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(biraj)
user=database.find('siddhant')
database.update(User(username='siddhant',name='Siddhant U',email='siddhantu@example.com'))

users=database.list_all()
print(users)


























#list of users for testcases
aakash=User('aakash','Aakash Rai','aakash@example.com')
biraj=User('biraj','Biraj Das','biraj@example.com')
hemanth=User('hemanth','Hemanth Jain','hemanth@example.com')
jadhesh=User('jadhesh','Jadhesh Verma','jadhesh@example.com')
siddhant=User('siddhant','Siddhant Sinha','siddhant@example.com')
sonaksh=User('sonaksh','Sonaksh Kumar','sonaksh@example.com')
vishal=User('vishal','Vishal Goel','vishal@example.com')

users=[aakash,biraj,hemanth,jadhesh,siddhant,sonaksh,vishal]

