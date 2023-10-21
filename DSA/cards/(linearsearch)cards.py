from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases
#Tests with example inputs and edge cases
tests=[]
#where query is in list
test={'input':{'cards':[13,11,10,7,4,3,1,0],'query':7},'output':3}
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


def locatecards(cards,query):
    #create a variable with position 0
    position=0
    print('cards:',cards)
    print('position:',position)
    #setup a loop to turn over the cards
    while position<len(cards):
        #check if element at current position matches query
        if cards[position]==query:
            #Answer found , return and exit
            return position
        #increment position
        position+=1
    return -1



















#store cards,query and expected output in a dictionary as k,v pairs for testing
"""
result=locatecards(cards,query)
print(result)
result==output

how to test
1) locatecards(test['input']['cards'],test['input']['query'])==test['output']
2)  locatecards(**test['input'])==test['output] 
"""