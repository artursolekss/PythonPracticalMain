numberUp = int(input("Enter the number\n"))

for number in range(2,numberUp + 1):
    prime = True

    for i in range(2,number):
        if(number % i == 0):
            prime = False

    if number > 1 and prime:
        print(number)