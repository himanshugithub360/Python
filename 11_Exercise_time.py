import time
timer = time.strftime('%H:%M:%S')
print(timer)

d1 = int(time.strftime('%H'))
d2 = int(time.strftime('%M'))
d3 = int(time.strftime('%S'))

if(4<d1<9):
    print("good morning")
elif(20<d1<23):
    print("good night")
    

