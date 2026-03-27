# these work with text

# file_name=input("enter the file name :" )

# f = open("file_handling.txt",'r')
# print(f.readline())
# f.close()


# it with we does not close the file it will automatically close

# with open("file_handling.txt",'r') as f:
#     print(f.read())


# when you want specific lines only
# with open("python.py", 'r') as e:
#     i = 0
#     # if we are not create ouside it's throe error name not fount that's why
#     line = e.readline()
#     while line:
#         line = e.readline()
#         print(line.split(","))
#         # if we want to exact particullar thing means    now its a list  if ' word' in  list print(line)
#         if i % 100 == 0:
#             op = input("you want more :")
#             if op.lower() == 'no':
#                 print("stop")
#                 break
#         i += 1


def add(x,y):
    return x+y