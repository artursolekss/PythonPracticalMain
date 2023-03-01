# a = True
# b = False

# print(a)
# print(b)

# a = 23
# b = 10
# c = a * b # c = multiply(a,b)
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b #c = concatenate(a,b)
# print(c)

# a = True
# b = False
# d = False
# # c = a and b #c = and(a,b) --->> if a is True AND b is True -->>> True, otherwise False
# c = a and b and d #and(a,b,d) -->> if all a,b,d are True --->>>True, otherwise False
# c = True and True and True
# #and(var1,var2,.......,varn) -->>if all var_ are True ->>>True, oterwise False
# c = True and True and True and True and True and True and True
# #and(var1,var2,.......,varn) = and(var1,and(var2,and(...)))
# print(c)

# a = True
# b = False
# c = True
# d = True

# result = a and (b and (c and d))

# res1 = c and d
# res2 = b and res1
# result = a and res2

# print(result)

# a = True
# b = False
# c = a or b #or(a,b) --->> True if a OR b is True, otherwise False;
# #a is False AND b is False -->>> False, otherwise True

# a = False
# b = False
# c = True
# d = False

# result = a or (b or (c or d))

# print(c)

#or(and(a,c),b) 

# a = True
# b = False
# c = True
# d = False

# # result = (a and b) or (c or d)# (True and False) or (True or False) ===> (False) or (True) ==>> False or True = True
# result = (a and b) or (c and d) #(True and False) or (True and False) ===> (False) or (False) ==> False or False = False
# print(result)

# a = False
# b = not a # not(a) = if a is True then b is False, if a is False then b is True
# print(b)

# a = True
# b = False
# c = True
# d = False
# result = (a and b) or (c and d)

# print(not result)

# De Morgan's laws
# boolean values var1, var2, ...., varn
# not(var1 or var2 or.... varn) = (not var1) and (not var2) and (not var3)... and (not varn)
# not(var1 and var2 and.... varn) = (not var1) or (not var2) or (not var3)... or (not varn)

a = True
b = True
c = False

# Same results (De Morgan's Law)
# result = not (a or b or c)
# result = not a and not b and not c

# Same results (De Morgan's Law)
# result = not (a and b and c)
# result = not a or not b or not c
# print(result)






