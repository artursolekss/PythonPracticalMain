elements = {1,2,3,42,1,4,52}
elements2 = {4,2,6,3,0,10,34}
# print(elements)#1,2,3,4,52,42
# elements.remove(3)
# print(elements)
# elements.add(0)
# print(elements)

# elements.add(34)
# elementsU = elements | elements2
# print(elementsU)
# elementsI = elements & elements2
# print(elementsI)
# elementsD = elements - elements2
# print(elementsD)

# elementsD2 = elements2 - elements
# print(elementsD2)

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
unique_set = set(my_list)
my_list = sorted(list(unique_set))
print(my_list)  # output: [1, 2, 3, 4, 5]
print(sorted(unique_set)) #converts set to list and sorts it