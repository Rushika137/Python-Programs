def todo():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        while True:
           try:
            num=int(input("enter a task value:"))
            if num>0 and num<5:
              break
            else:
                print("Enter a choice from 1 to 4.")
           except ValueError:
               print("invalid chice ,enter a numbber")         
        if num==1:
            task=input("enter the task:")
            with open("data.txt","a") as file: 
               file.write(task+"\n")

        elif num==2:
           with open("data.txt", "r") as file:
                             lines = file.readlines()
           if len(lines)==0:
                print("No tasks available!")
           else:
            with open("data.txt") as file:
               for number, line in enumerate(file, start=1):
                        print(number,".",line.strip())
            
        elif num==3:
             with open("data.txt", "r") as file:
                    lines = file.readlines()
             if len(lines)==0:
                    print("No tasks available!")
                    
             else:
                 for number, line in enumerate(lines, start=1):
                    print(number,".",line.strip())
                 while True:
                    try:
                       choice = int(input("Enter task number to delete: "))
                       if choice>0 and choice<=len(lines):
                             break
                       else:
                             print("enter from above choices")
                    except ValueError:
                             print("Invalid choice,choose a number")
                     

                    del lines[choice - 1]

                    with open("data.txt", "w") as file:
                           file.writelines(lines)
                    print("task completed sucessfully")
        elif num==4:
             print("Thank you,Come again!")
             return  
todo()