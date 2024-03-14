#String are immutable
b = "Himanshu "
print(len(b))
print(b)
print(b.upper())
print(b.lower())

a = " @@@@Himanshu@@ @@@@@@@ @@@@Himanshu @@ "
print(len(a))
print(a)

print(a.upper())

print(a.lower())

print(a.strip())  #The strip() method removes any white spaces before and after the string.

print(a.rstrip())

print(a.replace("Himanshu","Madhav")) #The replace() method replaces all occurences of a string with another string.

print(a.split(" ")) #The split() method splits the given string at the specified instance and returns the separated strings as list items.

str1 = "hello"
capStr1 = str1.capitalize()   #
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)     #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.


print(b.center(30))  #The center() method aligns the string to the center as per the parameters given by the user.
print(b.center(30,"."))

print(a.count("@"))  #The count() method returns the number of times the given value has occurred within the given string.

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))  #The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))  #We can even also check for a value in-between the string by providing start and end index positions.


str1 = "Their name is Dan. He is an honest man."
print(str1.find("is"))   #The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

str1 = "Their name is Dan. Dan is an honest man."
print(str1.index("is"))
# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Himanshu")) 

#The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

str2 = "Welcome Buddy"
print(str2.isalnum()) #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

str1 = "Welcome"
print(str1.isalpha()) #The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False

str1 = "hello world"
print(str1.islower()) #The islower() method returns True if all the characters in the string are lower case, else it returns False.

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace()) 
# The isspace() method returns True only and only if the string contains olny white spaces, else returns False.

str1 = "World Health Organization" 
print(str1.istitle())  #The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper()) #The isupper() method returns True if all the characters in the string are upper case, else it returns False.

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python")) #The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) #The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())  #The title() method capitalizes each letter of the word within the string.


