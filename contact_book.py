import json
import os
def load():
    if not os.path.exists("contacts.json"):
        return []
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
def contact_book():
  while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    while True:
        try:
            task = int(input("Enter your choice: "))

            if task > 0 and task < 7:
                break
            else:
                print("Enter a task between 1 and 6")

        except ValueError:
            print("Invalid choice. Enter a number from 1 to 6.")

    if task == 1:
        contacts = load()
        name =str(input("Enter the name: "))
        while True:
          number = input("Enter the mobile number: ")
          if len(number)==10 and number.isdigit():
              break
          else:
              print("Number not valid")
        while True:
          gmail = input("Enter Gmail ID: ")
          if "@gmail.com"  in gmail:
              break
          else:
              print("Email not valid")
        contact = {
            "Name": name,
            "Number": number,
            "gmail": gmail
        }        
        contacts.append(contact)
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
        print("Contact saved successfully!")
    elif task==2:
      with open("contacts.json", "r") as file:
            contacts = json.load(file)
      if len(contacts)==0:
          print("No contacts!")
      for j,i in enumerate(contacts,start=1):
          print(j,".","Name",":",i["Name"])
          print("   ","Number",":",i["Number"])
          print("   ","Gmail",":",i["gmail"])
    elif task==3:
        search=input("enter the name to search:")
        with open("contacts.json", "r") as file:
                contacts = json.load(file)
        for i in contacts:
             if i["Name"]==search:
                  print("Name"+":",i["Name"])
                  print("Number"+":",i["Number"])
                  print("Gmail"+":",i["gmail"])
                  break
        else:
            print("Not found!")    
    elif task == 4:
      contacts = load()
      if len(contacts)==0:
          print("no tasks avaible")
      else:
       for j, i in enumerate(contacts,start=1):
        print(j, ".", "Name:", i["Name"])
        print("   ","Number:", i["Number"])
        print("   ","Gmail:", i["gmail"])
       while True:
        try:
         contact_number = int(input("Enter contact number that has to be updated: "))
         if contact_number>0 and contact_number<=len(contacts):
           break
         else:
           print("enter number only of above contacts")
        except ValueError:
           print("please enter a number")
       print("1. Name")
       print("2. Number")
       print("3. Email")
       while True:
         try:
           update_number = int(input("Enter what you want to change: "))
           if update_number>0 and update_number<=3:
              break
           else:
              print("choose between 1 to 3")
         except ValueError:
           print("Invalid ,Please enter a number")
       for j, i in enumerate(contacts, start=1):
         if contact_number == j:
            if update_number == 1:
                value=str(input("enter the name:"))
                i["Name"] = value
                
            elif update_number == 2:
                while True:
                    value=input("enter the value:")
                    if len(str(value))==10 and value.isdigit():
                        break
                    else:
                        print("Invalid mobile number")
                i["Number"] = value
            elif update_number == 3:
                while True:
                  value= input("Enter Gmail ID: ")
                  if "@gmail.com"  in value:
                     break
                  else:
                     print("Email not valid")

                i["gmail"] = value
            else:
                print("Invalid option")
            break
       with open("contacts.json", "w") as file:
           json.dump(contacts, file, indent=4)
       print("Contact updated successfully!")
    elif task == 5:
       with open("contacts.json", "r") as file:
              contacts = json.load(file)
       if len(contacts)==0:
           print("No contacts!")
       for j, i in enumerate(contacts, start=1):
              print(j, ".", "Name:", i["Name"])
              print("Number:", i["Number"])
              print("Gmail:", i["gmail"])
       while True:  
        try:
         contact_number = int(input("Enter contact number that has to be deleted: "))
         if contact_number>0 and contact_number<=len(contacts):
            break
         else:
            print("enter number form above contacts")
        except ValueError:
           print("Invalid,enter a number")       
       contacts.pop(contact_number-1)
       with open("contacts.json","w") as file:
           json.dump(contacts , file , indent=4)
       print("task completed succesfully")
    elif task==6:
      print("Thank you,Come again!")
      break
contact_book()