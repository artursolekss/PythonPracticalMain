# for i in range(1,101):
#     print(i)

# sum = 0
# endvalue = int(input("Enter end value : "))
# for i in range(1,endvalue + 1):
#     sum += i #sum = sum + i

# print("Sum of all the values from 1 to " + str(endvalue) + " is " + str(sum))

# print("Calculate factorial")
# number = int(input("Enter the number : "))

# if number >= 0:
#     factorial = 1
#     for i in range(1,number + 1):
#         factorial *= i
#     print("Factorial of " + str(number) + " is " + str(factorial))
# else:
#     print("The value can't be negative")

# sum = 0
# endvalue = int(input("Enter end value : "))
# for i in range(-2,-(endvalue + 1),-2):
#     sum += i #sum = sum + i

# print("Sum of all even values from 1 to " + str(endvalue) + " is " + str(sum))

# end = int(input("Enter the end value : "))
# step = int(input("Enter the step : "))
# start = int(input("Enter the start value : "))
# for i in range(start,end,step):
#     print(i)

# list = ["Element 1","Element 2", "Element 3"]
# for element in list:
#     print(element)

# i = 0
# while i < 10:
#     i += 1#i = i + 1
#     print(i)

# i = 0
# while True:
#     i += 1#i = i + 1
#     print(i)

# i = 0
# while True:
#     i += 1#i = i + 1
#     print(i)
#     if i == 10:
#         break#breaks/exists the loop

#Prints even numbers only (skips odd numbers)
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 1:
#         continue#skip the code of while block below. goes to the next iteration
#     print(i)

# print("Calculate factorial")
# number = int(input("Enter the number : "))

# while number < 0:
#     number = int(input("Number can't be negative, please, enter again : "))

# factorial = 1
# for i in range(1,number + 1):
#     factorial *= i
# print("Factorial of " + str(number) + " is " + str(factorial))


#0 -2 -4 -6 -8 -10 ... -100
seq = range(0,-100,-2)
for i,j in enumerate(seq):
    print(i,j)
