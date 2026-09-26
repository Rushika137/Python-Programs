import json
import os
def load():
    if not os.path.exists("bank.json"):
        return []
    try:
        with open("bank.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
      return []
    
def management():
  while True:
    print("========================================")
    print("    "+"🏦 BANK MANAGEMENT SYSTEM"+"     ")
    print("========================================")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Update Account")
    print("7. Delete Account")
    print("8. View All Accounts")
    print("9. Exit")
    while True:
        try:
          task=int(input("enter your choice:"))
          if task>0 and task<=9:
            break
          else:
            print("please enter between 1 and 9")
        except ValueError:
           print("please,enter a integer!")
    def create_account():
        details=load()
        print("========== CREATE ACCOUNT ==========")
        while True:
           account_number=input("enter account number:")
           if len(account_number)==4 and account_number.isdigit():
              break
           else:
              print("please enter only 4 numbers")
        name =str(input("Enter the name: "))
        while True:
           number = input("Enter the mobile number: ")
           if len(number)==10 and number.isdigit():
                      break
           else:
                      print("Number not valid")
        while True:
            gmail = input("Enter Gmail ID: ")
            if gmail[-10:]=="@gmail.com":
                      break
            else:
                      print("Email not valid")
        while True:
          try:
             balance=int(input("enter balance:"))
             break
          except ValueError:
               print("please print balance in integers")              
        print("====Account created succesfully===")
        print("Account Number:",account_number)
        print("Name:",name)
        print("Balance:",balance)        
        detail={
             "Account Number":account_number,
             "Name":name,
             "Phone Number":number,
             "Gmail":gmail,
             "Account Balance":balance
        }
        details.append(detail)
        with open("bank.json","w") as file:
              json.dump(details,file,indent=4)
    def view_account(): 
         details=load()
         if len(details)==0:
              print("NO ACCOUNTS!")
              return
         while True:           
            account_number=input("enter account number to View:")
            if len(account_number)==4 and account_number.isdigit():
                break
            else:
                print("please enter only 4 numbers")
         for i in (details):
              if i["Account Number"]==account_number:
                   print("========VIEW ACCOUNT=========")
                   print("Name:",i["Name"])
                   print("Account Number:",i["Account Number"])
                   print("Phone Number",i["Phone Number"])
                   print("Gmail:",i["Gmail"])
                   print("Account Balance:",i["Account Balance"])
                   break
         else:
           print("NO Account Found!")
    def view_accounts():
         details=load()
         if len(details)==0:
               print("NO ACCOUNTS!")
               return
         print("========== VIEW ALL ACCOUNTS ==========")
         if len(details)==0:
              print("no accounts")
         print("Account No.     Name             Balance")
         print("------------------------------------------")
         for j,i in enumerate(details,start=1):
              print(j,".",i["Account Number"]  ,"      ",i["Name"],"        ",i["Account Balance"])
         print("------------------------------------------")
         print("Total Accounts=",len(details))
    def deposit_money():
         details=load()
         if len(details)==0:
               print("NO ACCOUNTS!")
               return
         print("====Deposit Money====")
         while True:
            account_number=input("enter account number to deposit:")
            if len(account_number)==4 and account_number.isdigit():
                         break
            else:
                         print("please enter only 4 numbers")
         for i in (details):
              if i["Account Number"]==account_number:
                  while True:
                   try:
                     amount = int(input("Enter amount to deposit: "))
                     if amount > 0:
                        break
                     else:
                        print("Amount must be greater than 0.")
                   except ValueError:
                       print("Please enter a valid amount.")
                  i["Account Balance"]+=amount
                  with open("bank.json","w") as file:
                                json.dump(details,file,indent=4)
                  print("$",f"{amount} is succesfully deposited.")
                  print("Current Balance:",i["Account Balance"])
                  return
         
         print("Account not found!") 
    
    def withdraw():
         details=load()
         if len(details)==0:
               print("NO ACCOUNTS!")
               return
         print("====Withdraw Money====")
         while True:
            account_number=input("enter account number to withdraw:")
            if len(account_number)==4 and account_number.isdigit():
                break
            else:
                print("please enter only 4 numbers")
         for i in (details):
               if i["Account Number"]==account_number:
                    while True:
                         try:
                            amount = int(input("Enter amount to withdraw: "))
                            if amount > 0:
                                   break
                            else:
                              print("Amount must be greater than 0.")
                         except ValueError:
                             print("Please enter a valid amount.")
                    balance=i["Account Balance"]-amount
                    if balance>0:
                            i["Account Balance"]=balance
                            with open("bank.json","w") as file:
                                 json.dump(details,file,indent=4)
                            print("$",f"{amount} is succesfully withdrawn.")
                            print("Current Balance:",i["Account Balance"])
                            return
                    else:
                         print("Insufficient Balance!")
                         return
               
               print("Account not found!")
    
    def Check():
         details=load()
         if len(details)==0:
               print("NO ACCOUNTS!")
               return
         while True:
              account_number=input("enter the account number:")
              if len(account_number)==4 and account_number.isdigit():
                  break
              else:
                  print("please enter only 4 numbers")
         for i in (details):
              if i["Account Number"]==account_number:
                   print("========== CHECK BALANCE ==========")
                   print("Name:",i["Name"])
                   print("Account Number:",i["Account Number"])
                   print("Current Balance:",i["Account Balance"])
                   return
              else:
                   print("no account found")
    def update():
         details=load()
         if len(details)==0:
               print("NO ACCOUNTS!")
               return
         while True:
          account_number=input("enter the account number:")
          if len(account_number)==4 and account_number.isdigit():
                    break
          else:
               print("please enter only 4 numbers")
         for i in (details):
               if i["Account Number"]==account_number:
                   print("1.Name")
                   print("2.Phone Number")
                   print("3.Gmail")
                   while True:
                     try:
                        update=int(input("enter the number to update:"))
                        if update>0 and update<=3:
                            break
                        else:
                            print("enter Valid Number!")
                     except ValueError:
                            print("Enter a number from above list")
                   if update==1:
                        print("Current Name:",i["Name"])
                        name=str(input("Enter new name:"))
                        i["Name"]=name
                        break
                   elif update==2:
                        print("Current Phone number:",i["Phone Number"])
                        while True:
                            number = input("Enter new mobile number:")
                            if len(number)==10 and number.isdigit():
                                        break
                            else:
                                print("Number not valid")
                        i["Phone Number"]=number
                        break
                   elif update==3:
                        print("Current Gmail:",i["Gmail"])
                        while True:
                            gmail = input("Enter new Gmail ID: ")
                            if gmail[-10:]=="@gmail.com":
                                    break
                            else:
                                 print("email not valid.")
                        i["Gmail"]=gmail
                        break
         with open("bank.json","w") as file:
               json.dump(details,file,indent=4)
         return "Updated succesfully!"
    def delete():
         details=load()
         if len(details)==0:
                       print("NO ACCOUNTS!")
                       return
         while True:
               account_number=input("enter the account number:")
               if len(account_number)==4 and account_number.isdigit():
                           break
               else:
                           print("please enter only 4 numbers")
               
         for j,i in enumerate(details,start=1):
                       if i["Account Number"]==account_number:
                        while True:
                         confirm = input(f"Are you sure you want to delete account {account_number}? (yes/n0): ").lower()
                         if confirm =="yes" or confirm =="no":
                              break
                         else:
                              print("enter yes or no")
                        if confirm =="yes":
                            details.pop(j-1)
                            with open("bank.json","w") as file:
                                 json.dump(details,file,indent=4)
                            print( "Task completed Succesfully!")
                            return
                        else:
                             print("Okay! Not Deleted")
                             return 
         print("Account Not Found")
    if task==1:
         create_account()
    elif task==2:
         view_account()
    elif task==3:
         deposit_money()
    elif task==4:
         withdraw()
    elif task==5:
         Check()
    elif task==6:
         update()
    elif task==7:
         delete()
    elif task==8:
         view_accounts()
    elif task==9:
         print("========THANK YOU!========")    
         break     
                             
         
    
management()