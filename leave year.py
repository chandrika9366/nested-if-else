year=int(input("enter year"))
if year%4==0:
    if year%100==0 and year%400==0:
        print("it is a century and leap year")
    elif year%100!=0:
        print("it is a leap year")
    else:
        print("it only centure year")
else:
    print("it is a simple year")       