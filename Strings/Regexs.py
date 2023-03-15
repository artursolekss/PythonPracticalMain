import re
# text = "The quick brown fox jumps over the lazy dog."
# match = re.search('fox', text)
# if match:
#     print("Found a match:", match.group())

#text@domain.country
# emailPattern = "^[a-zA-Z0-9][a-zA-Z0-9.]*[a-zA-Z0-9]@([a-z0-9]+\.)+[a-z]{2,}$"
# email = input("Enter the email\n")
# match = re.search(emailPattern, email)
# if match:
#     print("Pattern is correct")
# else:
#     print("Pattern is not correct")

phoneInput = input("Enter the phone:\n")
phonePattern = r'^((\+371|8)( ){0,1}){0,1}2[0-9]{7}$'
match = re.search(phonePattern,phoneInput)

if match:
    print("Pattern is correct")
else:
    print("Pattern is not correct")