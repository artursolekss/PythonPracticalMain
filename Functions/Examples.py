# name1 = input("Enter the name:\n")
# lastname1 = input("Enter the last name:\n")

# name2 = input("Enter the name:\n")
# lastname2 = input("Enter the last name:\n")

# name3 = input("Enter the name:\n")
# lastname3 = input("Enter the last name:\n")

# name4 = input("Enter the name:\n")
# lastname4 = input("Enter the last name:\n")

# def enterNameLastName():
#     name = input("Enter the name:\n")
#     lastName = input("Enter the last name:\n")
#     return name,lastName

# def printFullName(name="",lastName=""):
#     print(name + " " + lastName)

# name1,lastname1 = enterNameLastName()
# printFullName(name1,lastname1)

# printFullName(1,2)

# name2,lastname2 = enterNameLastName()
# printFullName(name2,lastname2)

# name3,lastname3 = enterNameLastName()
# printFullName(name3,lastname3)

# name4,lastname4 = enterNameLastName()
# printFullName(name4,lastname4)

# 1,2,3,4 -> 2,3
# 1,2,3,4,5 -> 3
# def getMiddleElement(l:list):
#     length = l.__len__()
#     if length == 0:
#         return None
#     elif length == 1:
#         return l[0]
#     else:
#         middlePoint = int(length / 2)
#         if length % 2 == 1:
#           return l[middlePoint]
#         else:
#             return l[middlePoint-1],l[middlePoint]#indexes start at 0

# def getMiddleElement(l:list)->list:
#     length = l.__len__()
#     if length == 0:
#         return [None]
#     elif length == 1:
#         return [l[0]]
#     else:
#         middlePoint = int(length / 2)
#         if length % 2 == 1:
#           return [l[middlePoint]]
#         else:
#             return [l[middlePoint-1],l[middlePoint]]#indexes start at 0

# midelements1 = getMiddleElement([1,5,3,6,4,7])
# print(midelements1)
# print(getMiddleElement([1,5,4,7]))

# print(4343)#acceptable by function

# def actions(*args):
#     for arg in args:
#         print(arg)


# actions(5,7,3,7,4,7)

# def actionsKW(**kwar):
#     print(kwar)
#     for key in kwar:
#         print(str(key) + " : " + str(kwar.get(key)))

# actionsKW(Name = "Arturs",LastName = "Olekss")

# def calculatePerimeter(a,b):
#     return 2 * (a + b)

# print(calculatePerimeter(2,8))

# def calculatePerimeter(a,b,c):
#     return a + b + c
# print(calculatePerimeter(2,8,6))

sqr = lambda x : x * x

print(sqr(4))