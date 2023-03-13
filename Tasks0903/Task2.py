for i in range(1,101):
    # if i % 3 == 0 and i % 5 == 0:
    #     print("FizzBuzz")

    printnumber = True
    if i % 3 == 0:
        print("Fizz",end="")
        printnumber = False

    if i % 5 == 0:
        print("Buzz",end="")
        printnumber = False

    if printnumber:
        print(i)
    else:#go to the next line
        print()

    # else:
    #     print(i)

#number / number2 = result (int) --> number - (result * number2)