#sample phone numbers 
phone_numbers={
    'Aakash':'9489484949',
    'Hemanth':'9595949494',
    'Siddhant':'9231325312',
}
print(phone_numbers)
#requesting value for key aakash
phone_numbers['Aakash']
phone_numbers['Vishal']='8787878787'
#updating phone no
phone_numbers['Aakash']='7878787878'

#iterating over dictionary and printing k,v pairs
for name in phone_numbers:
    print('Name:',name,'Phone Number:',phone_numbers[name])
    
#set max size for the hashtable list   
MAX_HASH_TABLE_SIZE=4096
#list of size MAX_HASH_TABLE_SIZE with all values None
data_list=[None] * 4096
print(len(data_list)==4096)
for item in data_list:
    assert item==None #should be true else asserion error
#operations for hashtable
class HashTable:
    def insert(self,key,value):
        #insert new k,v pair
        pass
    
    def find(self,key):
        #finds value associated with a key
        pass
    
    def update(self,key,value):
        #changes value associated with a key
        pass
    
    def list_all(self):
        #list all the keys
        pass
    
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
ord('x')

print(HashTable.get_index(data_list,'')==0)
print(HashTable.get_index(data_list,'Aakash')==585)
print(HashTable.get_index(data_list,'Don O Leary')==941)

#insert
#insert-get hash of key and store key value at that index
key,value='Aakash','7878787878'
idx=HashTable.get_index(data_list,key)
print(idx)#in this case the index is 585 so data is stored there
data_list[idx]=(key,value)#insert the key value at that index     
#same expression in a single line of code
data_list[HashTable.get_index(data_list,'Hemanth')]=('Hemanth','9595949494')#we def need to start doin this lol


#find 
#get hash of that key and look up that index
idx=HashTable.get_index(data_list,'Aakash')
key,value=data_list[idx]
print(value)

#list
#use list comprehension to get list of keys
