def binary_search(lo,hi,condition):
    """TODO -add docs"""
    #lo,hi=0,
    if lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        if result=='found':
            return result
        elif result=='left':
            hi=mid-1
        elif result=="right":
            lo=mid+1
    return -1
            