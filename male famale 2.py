age=int(input("enter age number"))
gender=input("enter gender")
ms=input("enter ms")
if gender=="f":
    print("she will work only in urban areas")
elif gender=="m":
    if age>20 and age<40 and ms=="yes":
        print("he may work in anywhere")
    elif age>40 and age<60 and ms=="yes":
        print("he will work only in urban areas")
    else:
     print("ERROR")