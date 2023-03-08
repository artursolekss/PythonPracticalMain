width = int(input("Enter the width (odd number) : "))

while width % 2 == 0:
    width = int(input("Please, enter an odd number : "))

middlePoint = int(width / 2) + 1
left = middlePoint
right = middlePoint
while left > 0:
    for i in range(1,width+1):
        if i >= left and i <= right:
            print(".",end="")
        else:
            print(" ",end="")
    left -= 1
    right += 1
    print("\n")#goes to the next line