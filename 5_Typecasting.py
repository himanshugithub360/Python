a = 1
b = 3
a1 = "1"
b1 = "3"

print(a + b)
print(a1 + b1)

print(type(a1))
print(type(int(a1)))

print(int(a1) + int(b1))   #---> Explicit typecasting
print(int(a1) + a)   #---> Explicit typecasting

#         Impilicit Typecasting
#       --------------------------
# While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

m = 8
print(type(m))

n = 6.0
print(type(n))

print(m+n)
print(type(m+n))
print(m-n)
print(m*n)
print(m/n)
print(m**n)
print(m//n)
