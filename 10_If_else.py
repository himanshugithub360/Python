a = int(input("Enter the age: "))
b=5
print(a)

# conditional operators 
# > , < , <= , >= , == , !=
print(a>18)
print(a>=18)
print(a<=18)
print(a<18)
print(a==18)
print(a!=18)

if(a>18):
    print("You are able to drive")
    print("yes")
else:
    print("You cannot drive")
    print("NO")

print("Yay!")

if(a-b>18) :
    print("yes")
else:
    print("no")

#           Nested if else
#        --------------------
    num= int(input("Enter the value : "))
    if(num<0) :
        print("Number is negative")
    elif(num==0):
        print("Number is zero")
    else:
        print("Number is postive ")
    print("Now its coming")


