###########################################################
################### Random Integer list ###################
###########################################################

from copy import deepcopy
from random import randint

def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst

  
foo = [1,2,3]
shuffle(foo)
# [3, 1, 2]

###########################################################
################### Random String list ###################
###########################################################

import random
word = raw_input("Enter a word: ")

charlst = list(word)        # convert the string into a list of characters
random.shuffle(charlst)     # shuffle the list of characters randomly
new_word = ''.join(charlst) # convert the list of characters back into a string

###########################################################
################# Random Letters in a Word ################
###########################################################

A=input("Enter a word:")
def Shuffle(A):
    ans=""
    B=list(A)
    for i in range(len(A)):
        a=random.randrage(0,len(A)
        ans+=B[a]
        B.pop(a)
    return ans
print(Shuffle(A))

###########################################################
################### Documentation #########################
###########################################################

## [Ref Link](https://docs.python.org/2/library/copy.html)
## A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
## A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
