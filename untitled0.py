# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 00:16:56 2022

@author: Bharath kuamr reddy
"""

#### real projects
### code for guessing the value
g = 1
a = int(input('guess the value:  '))
while (g == 33):
    a = int(input('guess the value:  '))
    g+=1
if a == g:
    print('cong , cortect!..')
elif a > g:
    print('larger')
else:
    print('smaller')
    
    
    
    
    
 #### ex-- calulator billing   
print('welcom to calc')
a = int(input('bill...?:   '))
b = int(input('tip % WILL TO hive:  '))
c = int(input('total no :   ')) 
e = round(((a*b)/(100*c)),5)  
print('you have to pay   {} Rs/--'.format(e))  
    
    
### pattern 
    
for i in range(1,6):            ### square
    for j in range(1,6):
        print(i,end=" ")
    print()
   
    
 for i in range(1,6):           ## rectangle
     for j in range(1,4):
         print('*',end=" ")
     print()
       
    
 for i in range(1,6):           ## right angle triangle(left)
     for j in range(i):
         print(i,end=" ")
     print()
     
    
for i in range(1,6):
    
   print(i*'*')
  
    
       
    
 for i in range(1,6):          ### right angle triangle(left downside)
     for j in range(6-i):
         print((6-i),end=" ")
     print()
     
     
         
for i in range(1,6):
    
   print((6-i)*'*')
  
    
       
 for i in range(1,6):
     
    print(" "*(6-i),'*'*i)
   
     

    
for i in range(1,6):
    for j in range(6-i):
        print(' ',end="")
    for k in range(i):
        print('*',end="")
    print()
    

for i in range(1,6):
    for j in range(6-i):
        print(' ',end="")
    for k in range(i):
        print(i,end=" ")
    print()
 
### dimond making patternn
    for i in range(1,10):
        for k in range(10-i):
            print(" ",end="")
        for j in range(i):
            print(i,end=" ")
        print()
    for i in range(1,9):
        for c in range(i+1):
            print(" ",end="")
        for j in range(9-i):
            print(9-i,end=" ")
        print()
       
   #....................................  
        
 for i in range(1,6):
     for k in range(6-i):
         print(' ',end="")
     for j in range(i):
         print('*',end="")
     print()
 for i in range(1,5):
     for k in range(i+1):
         print(' ',end="")
     for j in range(5-i):
         print("*",end="")
     print()
     
 #................................
 
   for i in range(1,10):
       for k in range(i):
           print(" ",end="")
       for j in range(10-i):
           print(i,end=" ")
       print()
   for i in range(1,9):
       for c in range(9-i):
           print(" ",end="")
       for j in range(i):
           print(9-i,end=" ")
       print()
      
for i in range(8):
    for j in range(1,i):
        print(j,end="")
    print()
 
    
 


### linear search
k = int(input('len of lst: '))
def search(lst,n):
    for i in  range(len(lst)):
        if n == lst[i]:
            print('found at index: ',i+1)
            break
    else:
        print('not found')
lst = []
for i in range(k):
    c = int(input('enter the values: '))
    lst.append(c)
    
lst
n = int(input('search element: '))
search(lst,n)

if n == lst[]

#### binary searching
  
def search(lis,n):
    l = 0
    u = len(lis)-1
    mid = (l+u)//2
    while l<=u:
        if n == lis[mid]:
            print('found at index', mid)
            break
        else:
            if n > lis[mid]:
                l = mid+1
            else:
                u = mid-1
    return False

        
lis = [1,3,99,0,6,4,3,88,54]
n = 88
search(lis,n)
print('not found')




def search(lis,n):
    l = 0
    u = len(lis)-1
    mid = (l+u)//2
    while l<=u:
        if n == lis[mid]:
            print('found at index', mid)
            
        else:
            if n > lis[mid]:
                l = mid+1
            else:
                u = mid-1
    return -1
    
lis = [1,3,99,0,6,4,3,88,54]
n = 88
search(lis,n)

####
n = int(input('value:  '))
d = []
for i in range(n):
    val = int(input('maarks:  '))
    d.append(val)
d
e = max(d)
f = d.remove(e)
g = max(f)

print('sec high score is',g)




c = [23,656,1,4,2,3]

c.sort()
c[-2]

### 10 coading challenge 
## 1.rad into deg
from math import pi

def deg(n):
    print("angle in deg {0}".format(n*180/pi))
     
n = float(input("enter angle in rad:  "))    
deg(n)

def deg(n):
    r = n*180/pi
    return r
     
n = float(input("enter angle in rad:  "))    
r = deg(n)
print(r)



########## passwordsetup 
import random as rd
c = int(input('length of pasword:  '))
list  = '12345678abcd@&%'
p =''.join(rd.choices(list,k=c))
print(p)

### table creation
x = int(input('table from: '))
y = int(input('table upto: '))
for i in range(x,y):
    for j in range(1,11):
        print('{0}*{1}={2}'.format(i,j,i*j))
    print("..........................")

## sum of n natural nos
def sum_n(k):
    r = k*(k+1)/2
    return r

c = int(input('enter no:  '))
r = sum_n(c)
print('sum of',c,'natural no is',r)

### roots of quad eqn
import cmath
a = int(input('enter a value: '))
b = int(input('enter b value: '))
c = int(input('enter c value: '))
d =  b*b-(4*a*c)
print(d)
if d == 0:
    print('roots are real and equal')
elif d > 0:
    print('roots are real and dist')
else:
    print('complex and img')
root1 =(-b+cmath.sqrt(d))/(2*a)
root2 =(-b-cmath.sqrt(d))/(2*a)
print(root1,"   ",root2)

## swap two values
a = int(input('enter a value: '))
b = int(input('enter b value: '))
a,b = b,a
print("a={0},b = {1} ".format(a,b))


### fibnocii series
n = int(input('no of val: '))
a = 100
b = 1000
print(a)
print(b)
for i in range(n-2):
    c = a+b
    print(c,"  ",i+3)
    a = b
    b = c

## anyonumus fun
#for i in range(11):
    f = [1,2,3,4,5,6,7,8,9]
    c = list(map(lambda i : 2**i,f))
    print(c)



for i in range(11):
    print(2**i)


terms = 10
result = list(map(lambda x: 2 ** x, range(terms)))
print(result)












