# strInput = input("Enter the string\n")

# for i in range(1,strInput.__len__()+1):
#     print(strInput[-i],end="")#input\n by default
# print()
# print(strInput.upper())
# print(strInput.lower())
# print(strInput.capitalize())
# print(strInput.center(30))
# print(strInput.replace("string","STR"))

# strToFormat = "Here is {} number"
# inputNumber = int(input("Enter the number\n"))

# print(strToFormat.format(inputNumber))

print("Here is the\t text")
print("Here is the\n text")
print('Here is the" text')
print('Here is the\\n text')
print(r"Here I use all the \n characters as \t the text \"")

text = "Powerful person"#Powerful*person*
text2 = "Powerful " + "person"
print(text == text2)

text = "Po"
text2 = text
text2 += "wer"
print(text)
print(text2)