# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:51:46 2021

@author: Bharath kuamr reddy
"""

 
s.capitalize()

s.upper()

s.rjust(20)
len(s.rjust(20))

w2 = input('enrter the name: ')
print(w2)
v = w2.strip()
print(v)


s = "I am using JAVA"

s = s.replace("JAVA", "Python")
s

c1 = [1, 3, 5, 7, 8]
c1

c1.pop(0)
c1
c1.pop(2) 
c1



teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}

teamA.union(teamB)
teamA.intersection(teamB)
teamA.difference(teamB)


lc = set(range(1,11))
lc 
for i in lc():
    print(i)

import math
for i in range(0,51):
    p = math.sqrt(i)
    if int(p) == float(p):
        print(p)






from array import *
k = array.array('i',[1,3,45,78,9,1])
for i in  k:
    print(i)



####  day 3 practice

    def oper(a,b):
        print(a+b)
        print(a-b)
        print(int(a/b))
        
  oper(5,8)

fl = lambda x: x**3
fl(5)

f = lambda x: x**3
  
lis = [2,5,7,5,2,34,67,222]    ##### using map function
c =list(map(f,lis))
c

lis = [2,5,7,5,2,34,67,222]    ##### using list function
f2 = lambda x : (x%2)== 0
a = list(filter(f2,lis))
a

from functools import reduce   #### using reduce function
lis = [2,5,7,5,2,34,67,222]
f4 = lambda x,y : x+y
sum = (reduce(f4,lis))
print(sum)

    
    
    
import random as rd
r = rd.randbytes(100)
r   
len(r)
r1 = rd.randint(1,100)    
r1
    
l1 = [222,333,111,444,666,555]

print(rd.choice(l1))

print(rd.choices(l1, k=100))



gender = ['Male', 'Female']

r = rd.choices(gender, k=10)
r
    
    
    
    #### random
import random as rd
r = rd.randint(0,10)
print(r)

list = [0,1,3,8,5]
rd.choice(list)

list = [0,1,3,8,5]
rd.choices(list, k = 10)

  #### NUMPY
import numpy as np
np.random.randint(5)

np.random.randint(0,10)

p = np.random.randint(0,5,10)
p

  ### numpy 1-D matrix-format
p[:]
p[0:]
p[3: ]
p[3:8]
p[3:-1]
p[3:-3]
p[ :-4]

   ### numpy 2-D matrix-format
c = np.random.randint(0,10,size=(5,10))
c
len(c)

c[0:, ]
c[3:4,]            ### 4th row calling
c[2:-1, ]          ### 3 and 4th rows calling
c
c[ : ,2:5]         ###  3,4,5 coloumns calling

c[-1, ]
c[ , -1]


c[1:4,2:6]
c[3: , 8: ]


### 3-D matrices 

k = np.random.randint(0,5,size =(5,4,5))  #### .
k

k[0]  ### to get 1 st section
k[2:, ]  ### calling from 2nd sec onwards
k[2:,1:3,3: ]

np.zeros((4,5),dtype = int)
np.zeros((4,5),dtype = float)

np.ones((4,5),dtype = int)
np.ones((4,5),dtype = float)


#### arange
h = np.arange(100)
h
h = np.arange(0,101)
h
h = np.arange(0,100,step = 2)
h
h = np.arange(0,100, 2,dtype = float)
h
h = np.arange(0,100,step = 3)
h.astype(float)

np.max(h)
np.min(h)
np.mean(h)
   
np.std(h)
  

### linespace
p=np.linspace(0,8,100) ### 100 is no of equal parts , default takes 50
p
print(type(p))

### concatination


a = np.random.randint(1,10,(2,5))
a
b = np.random.randint(1,8,(4,5))
b
c = np.concatenate([a,b])
c

#### ceil,float,trunc
a = np.floor([2.4,4.6])
a


a = np.ceil([2.4,4.6])
a

a = np.trunc([2.4,4.8])
a

a = np.round([2.4334567,4.63556],4)  ### 4 represents the no . of decimal points required
a

  #### creation of functions
  def profile(name,age,sal):
      print('name is', name)
      print('age is {0} and sal is {1}'.format(age,sal))
            
     
     
  profile( 'yke', 89,  89000) 
     
     
     def profile(name,age,sal):
         print('name is', name)
         print('age is {0} and sal is {1}'.format(age,sal))
               
        
        
     profile( age = 9, name = 'ykr', sal = 89000) 
        
        
     
     #### default arguments
     
 def profile(name = 'virat',age= 26,sal=1300):
     print('name is', name)
     print('age is {0} and sal is {1}'.format(age,sal))
           
    
    
 profile(name = 'ykr') 
 profile(age = 89)      


#### keyword variable length

def bio(name,**d):
    print(name)
    print(d)

bio(name = 'ykr',age =56,sex = 'M',mob= 824,hno = '34R')

## by using for loop            *d - used for store data without keywords
                                ### **d - used for store data with multiple keywordss
  
                                
  def bio(name,**d):
      print(name)
      for i,j in d.items():
          print(i , j)
  bio(name = 'ykr',mn = 6745,hno=74,sal = 273,job = 'whhfyw')



### problem
from numpy import *
u = array([1,2,3,5,7])
y = array([9,8,5,33,2])
for i,j in u:y:
    print(i+j)
    


## local and global variable

a = 10

def youtube(a):
    globe=a
    a =  5
    print(a)
    
youtube(a)
print(a)



### pass list in a function

list = [2,4,7,889,0,23,4,7,9,99]
def idef(list):
    even = 0 
    odd = 0
    for i in list:
        if i % 2==0:
            even =even+1
        else:
            odd=odd+1
    print(even,odd)
list = [2,4,7,889,0,23,4,7,9,99]
idef(list)
print('even is{0} odd is{1}'.format(even,odd))



list  = []
for i in range(1,11):
    a = input('enter nxt name: '  )
    list.append(a)
print(list)


n = int(input('enter the length of string : '))
list1 = []
for i in range(n):
    data = input('enter the nxt name:   ')
    list1.append(data)
print(list1)
    
def leka(list1):
    c = 0
    u = 0
    for i in list1:
        if len(i)>10:
            c = c+1
        else:
            u = u+1
    return c,u
print(list1)  
leka(list1)


print('even:{} and odd:{}'.format(c,u))





#### fibnocci series
 
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n):
        c = a+b
        print(c,i)
        a = b
        b = c



n = int(input('enter the max nos required:  '))
fib(n)



#### factorial of no

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
    
c = int(input('enter the fact of a no: '))
r = fact(n)
print(r)

########### recursion    max limit is 1000



def copy():
    print('hello')
    copy()

copy()

#### recursion (to know the  limit)
import sys
print(sys.getrecursionlimit())
def copy():
    print('hello')
    copy()

copy()

#### to improve the limit

import sys
sys.setrecursionlimit(30000)
print(sys.getrecursionlimit())
def copy():
    print('hello')
    copy()



### factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result = fact(5)
print(result)


n = int(input('enter the fact no:  '))
fact(n)




### exception handlingg
a = int(input('value: '))
b = int(input('value: '))
while True:
    try:
        print('file opend')
        print(a/b)
        print('well done')
        k = int(input('nxt value: '  ))
        c = input('str: ')
    except ZeroDivisionError as a:
        print('you cant dive with zero,  pls try again',      a)
    
    except ValueError as b:
        print('wrong input try again',   b)
        
    finally:
        print('file will closed')
    




def  fraction_of_one(divisor):
    value = 1/divisor # if divisor is zero, ZeroDivisionError will be raised
    return value
 
if __name__ == '__main__':
    while True:
        try:
            # Get input from the user.
            # if input is not a valid argument for int(), ValueError will be raised
            divisor = int(input("Enter a divisor: "))   
            # call our function to compute the fraction
            value = fraction_of_one(divisor)
        except (ValueError, ZeroDivisionError):
            print("Input can't be zero and should be a valid literal for int(). Please, try again!")
        else:
            print("Value: ", value)
            break


#### multi threading
from time import sleep
from threading import *
class number(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(1)

class square(Thread):
    def run(self):
        for i in range(10):
            print('hi')
            sleep(1)


t1 = number()
t2 = square()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()

print('bye')

#### file handling
f1 = open('fileH.txt','w')
f1.write('hi i am kameswar reddy\ni am doing my mtech in iit bbbsr\nin SMMME\nroll no 21mm06017\ni hailed from kurnnool,AP')
f1.close()


f2 = open('fileH.txt','r')
count = 0
for i in f2:
    print(i)
    count+=1
print('TOTAL LINES ARE:  {}'.format(count))
f2.close()


f2 = open('C:/Users/Bharath kuamr reddy/filecleaning.txt','r')
count = 0
for i in f2:
    print(i)
    count+=1
print('TOTAL LINES ARE:  {}'.format(count))



f3 = open('fileH.txt','a')
f3.write('i am scoring very less in 1st sem\nso i need to study more than what i do\ni will do wahterver i can \nso iwill fuck the bustardd')
f3.write('\nhi myself ykr \ni did my btech in ME\nfrom ksrmce')
f3.close()


### copying from one to anothe file
f4 = open('fileH.txt','a')
f5 = open('C:/Users/Bharath kuamr reddy/filecleaning.txt','r')
for i in f5:
    f4.write(i)
f5.close()
f4.close()

f4 = open('fileH.txt')
for i in f4:
    print(i)

### copying image file 
im = open('C:/Users/Bharath kuamr reddy/Downloads/IMG20211104190405 (1).jpg','rb')
type(print(im))
im1 = open('mypic.jpg','wb')
for i in im:
    im1.write(i)

l = open('mypic.jpg','rb')
print(l)

im.close()
l.close()



##### linear search
list = [5,3,4,52,0,8,1,101,302,303,2333,245,111]
print(list)
search = int(input('selct a no frm above:   '))
pos = 0
for i in list:
    pos+=1
    if i==search:
        print('no.exist at {}'.format(pos))
        break
else:
    print('no not found')

### creating a function

def find(list,search):
   #search = int(input('selct a no frm above:   '))
   pos = 0
   for i in list:
       pos+=1
       if i==search:
           print('no.exist at {}'.format(pos))
           break
   else:
       print('no not found')


list=[21,34,5,66,22,55,9000,10000]
search = 444444
find(list,search)

#### binary search
 #pos = -1
 def bsearch(list,n):
     l = 0
     u = len(list)-1
     while l<=u:
         mid = (l+u)//2
         if list[mid]==n:
             #globals()['pos'] = mid
            # return True
             print('no.found at {}'.format(mid+1))
             break
         else:
             if n>list[mid]:
                l = mid+1
             else:
                u = mid-1
     #return False
            
     else:
         print('sorrry,not found')
    
    

list = [3,44,55,500,550,589,6666,7777,88888,100000,123456]
n = 123456
bsearch(list,n)


## or 

if bsearch(list,n):
    print('found at {}'.format(pos+1))
else:
    print('not found')


##### BUBBLE SORT
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                #list[j],list[j+1]=list[j+1],list[j]
                ## or
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                  
        
list = [4,3,7,9,1,0,10,8,5,2,6]
sort(list)
list



### swapping
def swap1(a,b):
    a,b=b,a
    print('a',a)
    print('b',b)
swap1(2,3)
    
    
    
def swap2(x,y):    
    tem1 = x
    x = y
    y = tem1
    print(x)
    print(y)
swap2(2,3)
    
#### sorting by position


    def sortp(list):
        pos = -1
        for i in range(0,len(list)-1):
            pos+=1
            for j in range(i,len(list)-1):
                if list[pos]>list[j+1]:
                    list[pos],list[j+1]=list[j+1],list[pos]
        print(list)
     
    import numpy as np
    
    list = np.random.randint(0,100,size = 100)
   #or 
   ##list = [4,3,7,9,1,0,10,8,5,2,6,67,6,7]
    sortp(list)
    list   

#### reverse 



a = "kamesh is a younger one ,and he is from kurnool"
a.split(' ')
a.upper()
a.lower()
b = ['am','the','one']
'- @ dh'.join(b)


### split_and+join the string
def split_and_join(line):
    a = line.split(" ")
    result1 = '-'.join(a)
    return result1    

if __name__ == '__main__':
    line = input('enter the string:  ')
    result = split_and_join(line)
    print(result)

heros=['spider man','thor','hulk','iron man','captain america']
print('length is {}'.format(len(heros)))
heros.append('black panther')
heros
heros.remove('black panther')
heros.insert(4, 'black panther')
dir(heros)
heros
heros.sort()
heros


def prblm(stn,sub):
    count = 0
    for k in range(0,len(sub)):
        for i in range(0,len(stn)):
            if sub[k]==stn[i]:
                if sub[k+1]==stn[i+1]:
                    if sub[k+2]==stn[i+2]:
                       count+=1
    return count()
                                      
   

stn = 'ABCDCDC'
sub = 'CDC'
result = prblm(stn,sub)
print(result)

n = int(input('enter value: '))
arr = list(map(int, input().split()))
print(arr)

if __name__ == '__main__':
    import array
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(0,n):
        for j in range(0,n-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    res = arr
    for i in range(len(res)-1):
        if res[i+1]<res[i]:
            print(res[i+1])
            break
    

def swap_case(s):
    for i in s:
        if i == i.upper():
            i=i.lower()
        else:
            i = i.upper()
    return i
s = 'I am the KinhU'
swap_case(s)


def swap(r):
    c=''
    for i in r:
        if i==i.upper():
            c += i.lower()
        else:
            c += i.upper()
        return c
        
        #print(i,end="")
r = 'HackerRank.com presents "Pythonist 2".'
res = swap(r)
print(res)
   
def solve(s):
    new=''
    n = s.split()
    for i in n:
        i[0]=i[0].upper()
        new+=i
        return new
s = 'i am the good boy'
res = solve(s)
print(res)



# finding a sub-string in string

def scount(s,sb):
    count = 0
    for i in range(0,len(s)-len(sb)+1):
        if sb[ : ]==s[i:i+len(sb)]:
            count+=1
    return count


s = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair.'
sb= 'was'
len(sb)
res = scount(s,sb)
print(res)


### wraping a string

def wrap(s,w):
    n=0
    for i in s:
        n=n+1
        if n%w!=0:
            #return print(i,end="")
            c = print(i,end="")
        else:
           #return print(i,end=""),print()
            c = print(i,end="")
            print()
    return c

s='abcabcabcabcabwwert'
w = 3
res = wrap(s,w)
print(res)



def add(a,b):
    ad=a+b
    cu = a-b
    return ad,cu
res = add(z)

# recursive function
def add(n):
    if n==0:
        return n
    else:
        return n+add(n-1)
res = add(100)
print(res)



def sum(n):
    add = 0
    for i in range(n+1):
        add = add+i
    return add
print(sum(100))
    


def sumdigit(n):
    assert n>=0and int(n)==n,'no mustt be positve and integer'
    if n==0:
        return 0
    else:
        return n%10+sumdigit(n//10)
    
print(sumdigit(2222222222))


def sumd(n):
    assert str(n)==n,'must be string'
    s = 0
    k = str(n)
    for i in k:
        s+=int(i)
    return s
    
print(sumd(2222222222))

def powerN(base,exp):
    assert exp>=0 and int(exp)==exp,'exp must be positve integer'
    if exp == 0:
        return 1
    if exp==1:
        return base
    return base*powerN(base,exp-1)



print(powerN(2,100))

import array as arr
arr1 = arr.array('i',[2,3,98,4,7,8,8])
arr1
high = 0
for i in range(0,len(arr1)):
    #high = 0
    for k in range(i+1,len(arr1)):
        
        prod = arr1[i]*arr1[k]
        print(prod,arr1[i],arr1[k])
        if prod>=high:
            high =  prod
            pair = arr1[i],arr1[k]
print(high,pair)
        

clear()

import string
alpha = string.ascii_lowercase
c = 0
for i in alpha:
    c+=1
    if c<=4:
        print(i.center(5,"-"))


list1 = [1,2,3]
list2=[2,9,8]
for i in range(2):
    list1,
    list2=list(map(int,input().split()))
final = []
for i in list1:
    for j in list2:
        c=(i,j)
        final.append(c)
print(final)

import numpy as np
arr  = np.array([1,23,4,5,6,7,8,99,234])
np.reshape(arr(3,3))




list1=[]
for i in range(int(input('enter no of student:'))):
    #a = map(int(),input('roll no:  ').split())
    a = int(input('roll no:  '))
    list1.append(a)
print(list1)

list2=[]
for j in range(int(input('enter no of student:'))):
    #a = map(int(),input('roll no:  ').split())
    a = int(input('roll no:  '))
    list2.append(a)
print(list2)
res = set(list1)-set(list2)
len(res)


#hackerrank permutayions sum
x = 1
y = 1
z = 2
n = 3
    
final=[]
last_list=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            #print(i,j,k)
            final=final+[[i,j,k]]
            
#print(final)
for i in final:
    print(i)
    sum=0
    #print(i[0])
    for j in i:
        print(j)
        sum=sum+j
    if sum!=3:
        last_list=last_list+[i]
print(last_list)


a=400
b=600
c=1200
counter=0
days=[200,150,50,200,180]
for day in days:
    if a>=0:
        
        if a>0:
            a=a-day
        else:
            print(a)
            print('Master given course to A is completed')
            print(f'days took for a is {counter}')
            a=-80
    counter+=1   
    if b>0:
        b=b-day
    else:
        print("master given course to b is completed")
        print(f'days took for b is {counter}')
    if c>0:
        c=c- day
    else:
        print('master given course to c is completed')
        print(f'days took for c is {counter}')
   


