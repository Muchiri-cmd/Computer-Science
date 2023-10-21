#set max size for the hashtable list   
MAX_HASH_TABLE_SIZE=4096

class BasicHashTable:
    def __init__(self,max_size=MAX_HASH_TABLE_SIZE):
        self.data_list=[None] * max_size
    
    def get_valid_index(data_list,key):
        #take index returned by get_index
        idx=BasicHashTable.get_index(data_list, key)
        while True:
            #get key -value pair  stored at idx
            kv=data_list[idx]
            if kv is None:
                return idx#index is emtpy
            k,v=kv
            if k==key:
                return idx
            idx+=1
            #go back if youve reached end
            if idx==len(data_list):
                idx=0
                
    def get_index(data_list,a_string):
        #variable to store the result(updated after each iterarion)
        result=0 #initial result
        
        for a_character in a_string:
            #convert the character to the number (using ord)
            a_number=ord(a_character)
            #update result by adding the number
            result+=a_number
            
        #take the reminder of the result with the size of the data list
        list_index=result % len(data_list)
        return list_index
        
    def insert(self,key,value):
        #find index for the key using get index
        idx=BasicHashTable.get_index(self.data_list,key)
        #store k-v pair at the right index
        self.data_list[idx]=(key,value)
        
    def find(self,key):
        idx=BasicHashTable.get_index(self.data_list,key)
        #retrieve data stored at the index
        kv=self.data_list[idx]  
        #return the value if found,else None
        if kv is None:
            raise IndexError('key not found')
        else:
            key,value=kv
            return value
        
    
    def update(self,key,value):
        #find index for the key
        idx=BasicHashTable.get_index(self.data_list,key)
        #store the new k-v pair at the right index
        self.data_list[idx]=(key,value)
        
    def list_all(self):
        return[kv[0] for kv in self.data_list if kv is not None]
    
    
basic_table=BasicHashTable(max_size=1024)
print(len(basic_table.data_list)==1024)

#insert
basic_table.insert('Aakash','9999999999')
basic_table.insert('Hemanth', '8888888888')

#find
print(basic_table.find('Hemanth')=='8888888888')
#update
basic_table.update('Aakash', '7777777777')
#check updated value
print(basic_table.find('Aakash')=='7777777777')
#get list of keys
print(basic_table.list_all()==['Aakash','Hemanth'] )


#collisions
basic_table.insert('listen', 99)
basic_table.insert('silent', 200)
print(basic_table.find('listen'))

data_list2=[None]*MAX_HASH_TABLE_SIZE
#new key 'listen' should return expected index
print(BasicHashTable.get_valid_index(data_list2, 'listen')==655)
#insert a k,v pair for key listen
data_list2[BasicHashTable.get_index(data_list2,'listen')]=('listen',99)
#colliding key silent should give next result
print(BasicHashTable.get_valid_index(data_list2, 'silent')==656)
        