text = input("Enter the text:\n")
letter = input("Enter the letter:\n")
count = 0
for i in range(0,len(text)):
    if text[i] == letter:
        count += 1

print("There are " + str(count) + " occurences of "
      + letter + " in the text provided")