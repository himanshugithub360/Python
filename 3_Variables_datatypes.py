a = 1
b = True
c = "Himanshu"
d = None
a1 = 4
a2 = "Kumar"

print(a)
print(b)
print(c)
print(d)

print(a+b)
# print(a+c) -----> error int + str.  only same data types are added or concatinated
print(c + a2)

#     type() ------> for knowing the data type

print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of d is ", type(d))

list1= [3,45,5,[-3,0],["Himanshu","Kumar"]]  #------>it is mutable ie can be changed ,collection of different data types,ordered
print(list1)
print("The type of list1 is ", type(list1))


tuple1 = (("Welcome","Coder"),("parrot",'Boss'))  #------> it is immutable, ordered
print(tuple1)
print("The type of tuple1 is ", type(tuple1))

dict1 = {"name":"Himanshu","age":20,"vote":True} #------> unordered ,keyvalues pair
print(dict1)
print("The type of dict1 is ", type(dict1))

