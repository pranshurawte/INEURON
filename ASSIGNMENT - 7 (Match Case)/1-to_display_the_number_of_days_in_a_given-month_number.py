num = int(input("Enter the month : "))

match num :
    case num if num in (1 , 3 , 5 , 7 , 8 , 10 , 12 ) :
        print("31 days")
    case num if num in ( 4 , 6 , 9 , 11) :
        print("30 days")
    case 2 :
        print("28 or 29 days")
    case _ :
        print("Invalid Month number Entered ")    