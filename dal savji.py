day=input("enter day")
meal_time=input("enter meal time")
if day=="monday":
   if meal_time=="breackfast":
      print("pori sabji")
   elif meal_time=="lunce":
      print("sambhar rice")
   elif meal_time=="dinner":
      print("pulav soup")                        
   else:
      print("no meal")
elif day=="tuesday":
   if meal_time=="breackfast":
      print("sandwitch")
   elif meal_time=="lunce":
      print("alo paratha sabji")
   elif meal_time=="dinner":
      print("roti sabji")
   else:
      print("no meal")
else:
   print("none")   