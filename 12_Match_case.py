x = int(input("Enter the value of x : "))

match x:
    case 0: 
        print("X is zero")

    case 12:
        print("X is 12")
    
    case _ if (x!=23) :
        print("case is not 23")

    case _ if x == 50 :
        print("case is not 50")
        
    case _ :
        print("it default case of ",x)