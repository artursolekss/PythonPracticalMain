text = input("Enter the text:\n")
letters = {}#init the dictionary
for letter in text:#goes through all the characters of string
    count = letters.get(letter)#get the value, based on the key for the dictionary
    if count == None:#if there is no such key-value pair, then None is returneds
        letters[letter] = 1#add a new element to diction, where key is letter and value is the count of the letter
    else:
        count += 1 #incrememnt count recieved above
        letters[letter] = count #change the value for the count of the letter

print(letters)
print(letters.get("e"))#if the key exists, then it return the value mapped to the key
print(letters.get("<"))#if the key does not exist, then it returns None
print(letters["e"])
print(letters["<"])