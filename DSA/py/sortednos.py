from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases
import random
#test cases
#list of numbers in random order
test0={'input':{'nums':[4,2,6,3,4,6,2,1],},'output':[1,2,2,3,4,4,6,6],}
#list of numbers in random order
test1={'input':{'nums':[5,2,6,1,23,7,0,-12,12,-243],},'output':[-243,-12,0,1,2,5,6,7,12,23]}
#list of numbers already sorted
test2={'input':{'nums':[3,5,6,8,9,10,99],},'output':[3,5,6,8,9,10,99]}
#list sorted in descending order
test3={'input':{'nums':[99,10,9,8,6,5,3],},'output':[3,5,6,8,9,10,99],}
#list containing repeatng elements
test4={'input':{'nums':[5,-12,2,6,1,23,7,7,-12,6,12,1,-243,1,0]},'output':[-243,-12,-12,0,1,1,1,2,5,6,6,7,7,12,23]}
#An empty list
test5={'input':{'nums':[],},'output':[]}
#a list with 1 element
test6={'input':{'nums':[23]},'output':[23]}
#1 element repeated many times
test7={'input':{'nums':[42,42,42,42,42,42,42]},'output':[42,42,42,42,42,42,42]}
#really long list 
in_list=list(range(10000))
out_list=list(range(10000))
random.shuffle(in_list)
test8={'input':{'nums':in_list},'output':out_list}
tests=[test0,test1,test2,test3,test4,test5,test6,test7,test8]

print(in_list[:10])
print(out_list[:10])

def bubble_sort(nums):
    #create a copy of list to avoid changing original
    nums=list(nums)
    #repeat the process n-1 times
    for j in range(len(nums)-1):
        #print('iteration',j)
        #iterate over the array except last elem
        for i in range(len(nums)-1):
            #print(nums[i],nums[i+1])
            #compare numbers
            if nums[i]>nums[i+1]:
                #swap 2 elements
                nums[i],nums[i+1]=nums[i+1],nums[i]
    #return sorted list
    return nums


#input formats
nums=[4,2,6,3,4,6,2,1]
#output format
sorted_nums=[1,2,2,3,4,4,6,6]

nums0,ouput0=test0['input']['nums'],test0['output']
print('expected output:',ouput0)

result0=bubble_sort(nums0)

print('Actual Output:',result0)
print('Match:',result0==ouput0)









def sort(nums):
    pass

results=evaluate_test_cases(bubble_sort,tests)