def insertion_sort(nums):
    nums=list(nums)#make a copy
    for i in range(len(nums)):
        cur=nums.pop(i)#removes no temporarily from list
        j=i-1#ensures we stay within bounds start and end
        while j>=0 and nums[j]>cur:#as long as j in list and number at index j>popped
            j-=1#index j=j-1 moves before till no at j >current
        nums.insert(j+1,cur)#inserts no at index j+1(after index )if num at j is less 
    return nums

