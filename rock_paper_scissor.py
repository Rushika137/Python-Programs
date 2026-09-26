import random
def game(player_score,computer_score,round_number):
    print("-----ROCK_PAPER_SCISSOR-----")
    print(f"ROUND-{round_number}")
    choices=["ROCK","PAPER","SCISSOR"]
    print(choices)
    while True:
      player =str(input("enter your choice:")).upper()
      if player not in choices:
          print("invalid choice")
      else:
          break 
    computer=random.choice(choices)
    print("player:",player)
    print("computer:",computer)
    if player==computer:
        print("DRAW!")
    elif (
        (player == "ROCK" and computer == "SCISSOR")
        or (player == "PAPER" and computer == "ROCK")
        or (player == "SCISSOR" and computer == "PAPER")):
        print("player wins!")
        player_score+=1
    else:
        print("computer wins!")
        computer_score+=1
    round_number+=1
    return player_score,computer_score,round_number
player_score=0
computer_score=0
round_number=1        

while True:
    
    player_score, computer_score, round_number = game(player_score,computer_score, round_number)
   
    while True:
        again=input("do you want to play again:").lower()
        if again=="yes":
          while True:
            reset=input("do you want to reset score:").lower()
            if reset=="yes":
             player_score=0
             computer_score=0
             round_number=1
             break   
            elif reset=="no":
                break
            else:
                print("invalid  chioce,enter again")
          break
        elif again=="no":
            print("player:",player_score)
            print("computer:",computer_score)
            if player_score>computer_score:
                print("The overall winner is player,congrats!")
            elif player_score<computer_score:
                print("The overall winner is computer!,congrats")
            else:
                print("DRAW!")
            print("THANK YOU FOR PLAYING")
            exit()
        else:
            print("invalid choice,enter again")

        