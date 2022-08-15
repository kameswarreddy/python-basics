# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:06:21 2022

@author: Bharath kuamr reddy
"""

def bsearch(list,n):
    l = 0
    u = len(list)-1
     while l<=u:
         mid = (l+u)//2
        if list[mid]==n:
            return True
           # print('no.found at {}'.format(mid))
           # break
        else:
            if n>list[mid]:
                l = mid+1
            else:
                u = mid-1
    return False
            
    #else:
       # print('sorrry,not found')
    
    

list = [3,44,55,500,550,589,6666,7777,88888,100000]
n = 7777
if bsearch(list,n):
    print('found')
else:
    print('not found')
print('loeda')
