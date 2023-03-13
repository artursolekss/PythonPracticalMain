number1 = float(input("Enter number 1\n"))
number2 = float(input("Enter number 2\n"))

while True:
     operation = input("Enter operation (*,/,+.- or %)\n")
     if operation == "*":
           result = number1 * number2
     elif operation == "/":
        result = number1 / number2
     elif operation == "+":
        result = number1 + number2
     elif operation == "-":
         result = number1 - number2
     elif operation == "%":
         result = number1 % number2
     else:
         print("Operation is not correct")
         continue
     print("Result is " + str(result))
     break
