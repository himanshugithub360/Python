name = "Himanshu"  #int object cannot be iterable
for i in name:
    print(i)  #print character of name

s1 = "Madhav"
for m in s1:
     print(m,end=',')

print('\n')
colors =["red","black",'white']
for color in colors:
    print(color)  #print element of lists
    

fruits =["Mango","Apple","Orange"]  
for f in fruits:
     print(f)
     for f1 in f:
          print(f1)

    
for b in range(10): #print from 0-(n-1) by default
        print(b)

for m in range(3,10): #print from i to (n-1)
     print(m)        

for a in range(2,15,3):   # print from i to (n-1)  but gapping of j i.e. 2 to 15 but gapping of 3
     print(a)
     
