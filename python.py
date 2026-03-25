# def calculator():
#     a=int(input("Enter The Number: "))
#     b=int(input("Enter The Number: "))
#     print("Choose The Operation")
#     print('''
#           1. addition
#           2.subtraction
#           3.multiplication
#           4.true division
#           5.floor division
#           6.modules
#           7.Power
#           ''')
#     user=int(input("Enter The Operation: "))

#     if user==1:
#         print("addition",a+b)
#     elif user==2:
#         print("subtraction",a-b)
#     elif user==3:
#         print("mul",a*b)
#     elif user==4:
#         print("Truedivision",a/b)
#     elif user==5:
#         print("floordivision",a//b)
#     elif user==6:
#         print("modules",a%b)
#     elif user==7:
#         print("power",a**b)


# def calculator():
#     nums = list(map(int, input("Enter numbers (space separated): ").split()))

#     print("Choose The Operation")
#     print('''
#           1. Addition
#           2. Subtraction
#           3. Multiplication
#           4. True Division
#           ''')

#     user = int(input("Enter The Operation: "))

#     if user == 1:
#         print("Addition:", sum(nums))

#     elif user == 2:
#         result = nums[0]
#         for i in nums[1:]:
#             result -= i
#         print("Subtraction:", result)

#     elif user == 3:
#         result = 1
#         for i in nums:
#             result *= i
#         print("Multiplication:", result)

#     elif user == 4:
#         result = nums[0]
#         for i in nums[1:]:
#             result /= i
#         print("True Division:", result)

# calculator()

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


