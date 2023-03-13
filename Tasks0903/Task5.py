number = int(input("Enter the number\n"))

prime = True

for i in range(2,number):
    if(number % i == 0):
        prime = False

if number > 1 and prime:
    print("Number is prime")
else:
    print("Number is not prime")