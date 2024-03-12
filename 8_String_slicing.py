Person = "Madhav"
m1 = len(Person)
print(m1)

print(Person[3])

print(Person[0:6])  #[a:b] where a is the from where have to start printig AND b is the till b-1 index  have to print

print(Person[2:6])
print(Person[2:4])
print(Person[:4])
print(Person[0:-3])
print(Person[0:len(Person)-3])
# print(Person[-1:-3])   ------> error because person[-1:-3]==person[5:3] which os not possibe
# print(Person[len(person)-1:len(person)-3]) ------> erroe same
print(Person[-3:-1])
