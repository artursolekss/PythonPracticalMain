# agestr = input("Enter your age:")
# age = int(agestr)
age = int(input("Enter your age:"))
hasDrivingLicense = input("Do you have a driving license (y/n)?")

result = age >= 18 and hasDrivingLicense == "y"
print("You are able to drive : " + str(result))