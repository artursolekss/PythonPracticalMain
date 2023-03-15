# listInt = [1,2,3,4,5]

# for element in listInt:
#     print(element)

# fruits = ["apple","banana","pinapple","orange"]

# for i in range(0,fruits.__len__()):
#     if i == 0:
#         print(fruits[0],end="")
#     else:
#         print(",",fruits[i],end="")

# for fruit in fruits:
#     print(fruit,end=",")#fruit
    # print(fruit)#fruit + "\n"

# print("apple\nbanana\npinapple")

# list = ["element1",1,True]
# for element in list:
#     print(element)

# print(list)

# list = [[1,2,3,4],["element1","element2","element3","element4"]]
# for element in list:
#     print(element,end="")#element + \n

#list[0] = [1,2,3,4]

# subList = list[0]
# print(subList[0])

# secondList = list[1]
# print(secondList[0])

# list = []
# list.append("Element1")#["Element1"]
# list.append("Element2")#["Element1","Element2"]
# # for element in list:
# #     print(element)
# # print(list)

# list.pop(0)
# print(list)

# list = [1,2,3,4,"Element",5,6,"Element",7,"Element",8,"Element"]
# list.remove("Element")
# list.count()
# print(list.count("Element"))
# count = list.count("Element")

# # for i in range(0,count):
# #     list.remove("Element")

# while count > 0:
#     list.remove("Element")
#     count -= 1# count = count - 1

# list.pop(1)
# print(list)

# index = -1#not found
# countFound = 0
# for i in range(0,list.__len__()):
#     if list[i] == "Element":
#         countFound += 1
#     if countFound == 3:
#         list.pop(i)
#         break

# print(list)

#
# listA = [1,2,3,4]
# listB = listA
# listA.append(5)
# print(listB)
# listB.append(6)
# print(listA)

# list = [1,2,3,4]
# list += [5,6]
# print(list)

# listA = [1,2,3,4]
# listB = listA[:]#copy
# listB.append(5)

# print(listA)
# print(listB)


# listB = listA[:3]
# print(listB)

# list = []

# print("Enter the values below")
# while True:
#     element = input("Enter the number\n")
#     if element == "":
#         break
#     number = float(element)
#     list.append(number)


# sum = 0

# for number in list:
#     sum += number

# # average = sum / list.__len__()
# average = sum / len(list)
# print("Sum of all the elements is ",sum)
# print("Average value",average)

# print(list)

# list2 = []
# for element in list:
#     elementNew = element + 1
#     list2.append(elementNew)

# list2 = [element + 1 for element in list]
# print(list2)
# list3 = [element ** 2 for element in list]#element  ** 2 == element * element
# print(list3)

#["a","b","c"] + ["d","e"] = ["a","b","c","d","e"]

# listA = []
# listB = []

# listA.append("A")
# listA.append("B")
# listA.append("C")

# listB.append("A")
# listB.append("B")
# listB.append("C")

# print(listA == listB)

# listA.extend(listB)
# print(listA)

# print(listA.index("B"))
# listB = listA.copy()
# listB = listA[:]

# listA.reverse()
# listA.pop(0)#["B","C"]
# listA.pop(1)
# listA = listA[1:2]
# print(listA)

# list = [1,2,3,4,5,6,7,8]
# list = list[1:7]
# print(list)

# list = ["Element1","ELement0","Element3"]
# list.sort()
# print(list)

list = [1,8,29,19]
# list2 = list * 6 #all the elements are repeated 6 times
# print(list2)

sumOfAll = sum(list)
print(sumOfAll)

print(min(list))
print(max(list))
print(sum(list)/len(list))#average

