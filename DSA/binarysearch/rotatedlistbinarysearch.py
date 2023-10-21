from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases
def count_rotations_binary(nums):
    lo,hi=0,len(nums)-1
    while lo<=hi:
        mid=(hi+lo)//2
        mid_number=nums[mid]
        #logging line
        print("lo:",lo,"hi:",hi,"mid:",mid,"mid_number:",mid_number)
        if mid>0 and mid_number < nums[mid-1]:
            return mid
        elif mid>nums[mid-1]:
            hi=mid-1
        else:
            lo=mid+1
    return 0
            
#test cases
test0={'input':{'nums':[19,25,29,3,5,6,7,9,11,14],},'output':3}#base test
test1={'input':{'nums':[4,5,6,7,8,1,2,3],},'output':5}#list of size 8 5 rotations
test2={'input':{'nums':[1,2,3,4,5,6],},'output':0}#list wasnt rotated at all
test3={'input':{'nums':[7,3,5],},'output':1,}#list rotated only once 
test4={'input':{'nums':[2,3,4,5,1]},'output':4}#list that wa rotated n-1 times
test5={'input':{'nums':[3,5,7,8,9,10],},'output':0}#list that was rotated n times (original)
test6={'input':{'nums':[],},'output':0}#can an empty list be rotated?
test7={'input':{'nums':[1],},'output':0}#can a list with one element be rotated?

tests=[test0,test1,test2,test3,test4,test5,test6,test7]
evaluate_test_cases(count_rotations_binary,tests)
nums0=test0['input']['nums']
output0=test0['output']
result0=count_rotations_binary(nums0)
print(result0==output0)