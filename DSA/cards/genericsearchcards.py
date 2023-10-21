from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases
tests=[]
test=({'input':{'cards':[13,11,10,7,4,3,1,0],'query':7},'output':3})

tests.append(test)
tests.append(test)#appends above test to tests,list
#where query is first element
tests.append({'input':{'cards':[13,11,10,7,4,3,1,0],'query':1,},'output':6,})
#where query is last element
tests.append({'input':{'cards':[4,2,1,-1],'query':4,},'output':0,})
#where query is last element
tests.append({'input':{'cards':[3,-1,-9,-127],'query':-127,},'output':3,})
#where query is only element
tests.append({'input':{'cards':[6],'query':6,},'output':0})
#where query not in cards return -1
tests.append({'input':{'cards':[9,7,5,2,-9],'query':4,},'output':-1})
#cards empty
tests.append({'input':{'cards':[],'query':7,},'output':-1})
#numbers repeat in cards
tests.append({'input':{'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],'query':3,},'output':7})
#query repeated returns first 
tests.append({'input':{'cards':[8,8,6,6,6,6,6,3,2,2,2,0,0,0],'query':6},'output':2})

def binary_search(lo,hi,condition):
    """TODO -add docs"""
    while lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        elif result=="right":
            lo=mid+1
    return -1
        
def locate_cards(cards,query):
    def condition(mid):

        if cards[mid]==query:
            if mid>0 and cards[mid-1]==query:
                return 'left'
            else:
                return 'found'
        elif cards[mid]<query:
            return 'left'
        else:
            return 'right'
            
    
    return binary_search(0,len(cards)-1,condition)

evaluate_test_cases(locate_cards,tests)