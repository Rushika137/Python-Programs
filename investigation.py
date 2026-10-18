import json
def investigate():
    
        
while True:
    print("1. Investigate Mansion")
    print("2. Interview Suspect")
    print("3. View Clues")
    print("4. View Suspects")
    print("5. Make Final Accusation")
    print("6. Exit")

    choice = input("What do you want to do: ")

    if choice == "1":
        investigate()

    elif choice == "2":
        interview()

    elif choice == "3":
        show_clues()

    elif choice == "4":
        show_suspects()

    elif choice == "5":
        accusation()

    elif choice == "6":
        break

    else:
        print("Invalid choice")

