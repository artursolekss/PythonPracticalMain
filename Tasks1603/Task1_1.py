text = input("Enter the text:\n")
letters = []
lettersCount = []
for i in range(0,len(text)):
    letterExist = False
    if text[i] == " ":
        continue
    for j in range(0,len(letters)):
        if letters[j] == text[i]:
            lettersCount[j] += 1
            letterExist = True
            break
    if not letterExist:
        letters.append(text[i])
        lettersCount.append(1)

for i in  range(0,len(letters)):
    print(letters[i] + " : " + str(lettersCount[i]))