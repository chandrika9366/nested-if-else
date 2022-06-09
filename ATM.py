atm_cart=input("enter atm_cart")
if atm_cart=="right side" or atm_cart=="Right side":
   language=input("enter language")
   if language=="hindi" or language=="Hindi" or language=="english" or language=="English":
      pin=int(input("enter pin num"))
      if pin>=1000 and pin<=9999:
         type_option=input("enter type_option")
         if type_option=="withdraw" or type_option=="Withdraw":
            account_type=input("enter account_type")
            if account_type=="saving" or account_type=="Saving":
               press_key=input("enter press_key")
               if press_key=="ok" or press_key=="Ok":
                  amount=int(input("enter amount"))
                  if amount>=500 and amount<=20000 and amount%500==0:
                     a=amount//2000
                     b=amount%2000
                     c=b//500
                     print("notes of 2000",a,"notes of 500",c,) 
                     press=input("enter complate press")
                     if press=="cancel" or press=="Cross":
                        print("your transaction is succesfull")
                     else:
                        print("cancel button not press")
                  else:
                      print("amount not available")
               else:
                  print("press not ok")
            else:
               print("error")
         elif type_option=="balance enquiry" or type_option=="Balance enquiry":
                account_type=input("enter account_type")
                if account_type=="saving" or account_type=="saving":
                   account_no=int(input("enter account_no"))
                   if account_no>=100000000000 and account_no<=999999999999:
                      press_key=input("enter press_key")
                      if press_key=="ok" or press_key=="ok":
                          print("balance checking succesfull")
                      else:
                          print("ok button not prees")
                   else:
                      print("account number not correct")
                else:
                   print("error")
         elif type_option=="diposit money" or type_option=="Diposit money":
               account_type=input("enter account_type")
               if account_type=="current" or account_type=="Current":
                  account_no=int(input("enter account no"))
                  if account_no>=100000000000 and account_no<=999999999999:  
                   money=int(input("enter money"))
                   if money>=1 and money<=1000000000:
                      press_key=input("enter press key")
                      if press_key=="ok" or press_key=="Ok":
                            print("you diposit money succesfull")
                      else:
                         print("press not ok")
                   else:
                      print("money not transfar") 
                  else:
                     print("wrong account no")
               else:
                  print("error")
         elif type_option=="bill pay" or type_option=="Bill pay":
               account_type=input("enter account_type")
               if account_type=="current" or account_type=="current":
                  account_no=int(input("enter account no"))
                  if account_no>=100000000000 and account_no<=999999999999:
                        money=int(input("enter money"))
                        if money>=1 and money<=1000000000:
                           press_key=input("enter press key")
                           if press_key=="ok" or press_key=="Ok":
                                 print("bill transaction complate")
                           else:
                              print("press not ok button")
                        else:
                           print("money not available")
                  else:
                     print("wrong account number")
               else:
                 print("type_option error")
         else:
            print("type option error")
      else:
         print("wrong pin number")
   else:
      print("not correct language")
else:
    print("wrong side")