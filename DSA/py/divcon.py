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

def merge(nums1,nums2,depth=0):
    merged=[]
    print (' '*depth,'merge:',nums1,nums2)
    #indices for iteration
    i,j,merged=0,0,[] #pointers for the 2 lists
    #loop over the two lists
    while i<len(nums1)and j<len(nums2):
        #include smaller element in the result and move to next element
        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
    #get the remaining parts
    nums1_tail=nums1[i:]
    nums2_tail=nums2[j:]
    #return final merged array
    return merged+nums1_tail+nums2_tail    

def merge_sort(nums,depth=0):
    print(' '*depth,'merge_sort:',nums)
    #terminating condition (list of 0 or 1 elements)
    if len(nums)<=1:
        return nums  
    mid=len(nums)//2
    #split the list into 2 halves
    left=nums[:mid]
    right=nums[mid:]
    #solve the problem for each half recursively
    left_sorted,right_sorted=merge_sort(left),merge_sort(right)
    #comine results of the 2 halves
    sorted_nums=merge(left_sorted,right_sorted)
    return sorted_nums
    
    
merge([1,4,7,9,11],[-1,0,2,3,8,12])
nums0,output0=test0['input']['nums'],test0['output']
print('input:',nums0)
print('Expected output:',output0)
result0=merge_sort(nums0)
print('Actual Output:',result0)
print('Match:',result0==output0)

#evaluate_test_cases(merge_sort, tests)