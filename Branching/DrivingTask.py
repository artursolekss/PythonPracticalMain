age = int(input("Enter your age:"))
hasDrivingLicense = "n" #default value
if age > 17:
  hasDrivingLicense = input("Do you have a driving license (y/n)?")
  
result = hasDrivingLicense == "y" and age >= 18

# if result:
#   print("You are able to drive")
#   print("Congradulations!")
  
# print("THIS CODE WILL ALWAYS BE PRINTED") #this statememnt does not belong to any if block

# if not result:
#   print("You are not able to drive")
#   print("It's sad!")

# if result:
#   print("You are able to drive")
#   print("Congradulations!")
# elif age > 17:
#   print("You can already get your driving lincese")
# else:#this block is executed if results is False
#   print("You are not able to drive because you are too young")
#   print("It's sad!")

# if result:
#   print("You are able to drive")
# else:
#   print("You are not able to drive")

print("You are able to drive") if result else print("You are not able to drive")