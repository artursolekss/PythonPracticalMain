# elements = [1,5,-10,5,8,3]
elements = ["a","c","e","z"]
#n = len(elements)
#bubble sort
for i in range(0,len(elements)): #n * n
    for j in range(0,len(elements)-i-1):
        if elements[j] < elements[j+1]:
            elements[j],elements[j+1] = elements[j+1],elements[j]
        print(elements)

print(elements)
