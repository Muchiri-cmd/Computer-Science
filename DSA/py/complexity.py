def quicksort(nums,start=0,end=None):
    #print('quicksort',nums,start,end)
    if end is None:
        nums-list(nums)
        end=len(nums-1)
        
    if start<end:
        pivot=partitions(nums,start,end)
        quicksort(nums,start,pivot-1)
        quicksort(nums,pivot+1,end)
        
    return nums