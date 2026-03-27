
# copy
# l=[1,2,[3],'hello']
# m=l                 # normal copy
# print(id(l),id(m))

# n=l.copy()          # shallow copy
# print(id(n))

# n[2][0]=4

# print(n,l)

# p=l[::1]            # shallow copy

# p[2][0]=5
# print(l,p)


# import copy         # deep copy
# d=copy.deepcopy(l)

# d[0]=5
# print(d,l)


# for i in range(0,len(l)):
#     print(id(l[i]))

# print()
# for i in range(0,len(n)):
#     print(id(n[i]))
# print()
# for i in range(0,len(d)):
#     print(id(d[i]))


# switch case in python  -- match

# var=10

# match var:
#     case 1:
#         print("hello")
#     case 10:
#         print("This Match in python  Or Other inn switch case ")




#  Exceptional Hand;ing in python 
# import sys

# try :
#     c= a+b
# except :
#     print(sys.exc_info()[0])



# import sys   #  it contains  error for system this a modul



# import sys
# a=10
# b=[1,2,3,4]
# c=5
# try:
#     c = a+ b[5]
# except  NameError as e:
#     print("name error")
#     print(e)
# except IndexError as e:
#     print("index  error")
#     print(e)
# else:
#     print("all good after the if try block was success")
# finally:
#     print("all done")




# import sys

# a=10
# try:
#     a=a/0
# except Exception as e :   # exception having all type of error
#     print(e)


# b=0
# if b==0:
#     raise Exception("zero division error")


# a = 10
# b = int(input("Enter the b :"))

# try:
#     c= a/b
#     print(c)
# except Exception as e:
#     print(e)



# n=5

# for i in range(n):
#     for j in range(n):
#         if i+j > n:
#             print("*",end='')
#         elif i < j :
#             print("*",end='')
#     print()


# pyramid patter

# n=5
# for i in range (n):
#     print(" "*(n-i-1)+"*"*(2*i+1))

# n=5
# val=65
# for i in range(n):
#     for j in range(n):
#         print(chr(val),end='')
#         val+=1
#     print()
#     val+=1

# d={"one":2,"two":2}
# for i in iter(d):
#     print(i)

#  internally does 
# it = iter(d)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break



# anagram

# s1='eat'
# s2='bat'

# print(sorted(s1),sorted(s2))


# from collections import Counter
# print(Counter(s1) == Counter(s2))

# s1 = "eat"
# s2 = "tea"

# # Step 1: length check
# if len(s1) != len(s2):
#     print(False)
# else:
#     count = {}

#     # Step 2: count characters in s1
#     for ch in s1:
#         if ch in count:
#             count[ch] += 1
#         else:
#             count[ch] = 1

#     # Step 3: reduce using s2
#     for ch in s2:
#         if ch in count:
#             count[ch] -= 1
#         else:
#             print(False)
#             break

#     # Step 4: check all values = 0
#     for val in count.values():
#         if val != 0:
#             print(False)
#             break
#     else:
#         print(True)



# *a,b,c=[1,2,4,5,7]
# print(a,b,c)



# how accept the value store inside the variable in the form of dict
# def add(**kwargs):
#     return kwargs

# print(add(a=10,b=20))


# def add(*,a,b,c):
#     return a,b,c

# print(add(a=10,c=30,b=40))

# def add(*args,**kwargs):
#     return args,kwargs

# print(add(1,2,3,4,5,a=10))


# scope
# global

# x=10
# def fun():
#     x=20
# print(x)


# x=10
# def fun():
#     x=20
#     print(x)
#     def inner():
#         nonlocal x
#         x+=30
#     inner()
#     print(x)
# fun()


#  this is clouser scope under enclosing 



# def adder(x):
#     def inner(y):
#         return x+y
#     return inner

# result=adder(10)
# print(result)
# print(result(20))

# def outer(x):
#     def add(y):
#         return x+y
#     def sub(y):
#         return x-y
#     return add,sub
# add_,sub_=outer(10)

# print(add_(50))
# print(sub_(50))




# lambdaw function


# print((lambda var : var > 3)(5))
# print((lambda x : "yes" if x >3 else "no")(5))
# result = lambda x :"yes" if x > 3 else "no"
# print(result(5))





#                        map




# number=[1,2,3,4,5]
# print(list(map(lambda x : x+10,number)))

# def square(x):
#     return x*x

# print(list(map(square,number)))


# filter function
# def greater(x):
#     return x > 2
    
# print(list(filter(greater,number)))



#           MOdules



# from file_handling import add
#import math

# f=math.factorial(5)
# print(f)

# print(math.lcm(6,18))

# print(math.floor(2.9))

# l=[x for x in range(1,100)]

# def nums(l):
#     for i in l:
#         yield i
# print(list(nums(l)))




 #              BEST EXAMPLE For Genarator

# it execute one one time come and store value go out side resume function ---this is the main differentc

# l=[x for x in range(1,100)]

# def d_numbers(l):
#     for o in l:
#         print("every time it will come ")
#         yield o*2

# for i in d_numbers(l):
#     print(i)



# see this different yield and return   

#--- it runs fully once return stop execution that all matter keeps all data 
# def normal(l):
#     out=[]
#     for i in l:
#         print("normla function")
#         out.append(i*2)
#     return out

# for i in normal(l=[10,20,30,40,50]):
#     print(i)

# decorator :


# def outer(func):
#     def inner(*args,**kwargs):
#         print("hello")
#         func()
#         print("welcome")
#     return inner

# @outer
# def poo():
#     print("poovarsan")

# outer(poo())



# # recusive 
# def num(l):
#     out=[]
#     for i in l:
#         if isinstance(i,list):
#             out.extend(num(i))
#         else:
#             out.append(i)
#     return out

# print(num(l=[1,[2,3,[4,5,[6,7]]]]))




# def flatten(l):
#     for i in l:
#         if isinstance(i, list):
#             yield from flatten(i)
#         else:
#             yield i


# oops 
