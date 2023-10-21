#set max size for the hashtable list   
MAX_HASH_TABLE_SIZE=4096

class ProbingHashTable:
    def __init__(self,max_size=MAX_HASH_TABLE_SIZE):
        #create a list of size max_size with all values none
        self.data_list=[None] * max_size
    
    def get_valid_index(data_list,key):
        #take index returned by get_index
        idx=ProbingHashTable.get_index(data_list, key)
        while True:
            #get key -value pair  stored at idx
            kv=data_list[idx]
            if kv is None:
                return idx#index is emtpy
            k,v=kv
            if k==key:
                return idx
            idx+=1
            #go back if youve reached end keep looping 
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
        #find index for the key using get_valid_index
        idx=ProbingHashTable.get_valid_index(self.data_list,key)
        #store k-v pair at the right index
        self.data_list[idx]=(key,value)
        
    def find(self,key):
        #find index for key using get_valid_index
        idx=ProbingHashTable.get_valid_index(self.data_list,key)
        #retrieve data stored at the index
        kv=self.data_list[idx]  
        #return the value if found,else None
        return None if kv is None else kv[1]
        
    def update(self,key,value):
        #find index for the key
        idx=ProbingHashTable.get_valid_index(self.data_list,key)
        #store the new k-v pair at the right index
        self.data_list[idx]=(key,value)
        
    def list_all(self):
        return[kv[1] for kv in self.data_list if kv is not None]
    
#create new hash table
probing_table=ProbingHashTable()
    
#insert a value
probing_table.insert('listen', 99)
probing_table.insert('silent', 200)
#check the value
print(probing_table.find('listen')==99 and 
      probing_table.find('silent')==200)
#update a key
probing_table.update('listen', 101)
print(probing_table.find('listen')==101)
print(probing_table.list_all())