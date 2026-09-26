import random
def hangman():
    guessed_letters=[]
    print("================================")
    print("       ","HANGMAN GAME","       ")
    print("================================")
    print("Guess the hidden Word!")
    words=["fromvilla","dark","family","sheldon","borderland"]
    word=random.choice(words)
    answer=list(word)
    lives=6
    display=["_"]*len(word)
    def displaying():
     for i in (display):
        print(i,end=" ")
    while lives>0 :
        displaying()
        print("\n\n"+f"You have {lives} more lives")
        print("\n"+"Guessed Letters:",end="")
        for i in guessed_letters:
            print(i,end=",")
        while True:
          letter=str(input("\n\n"+"enter the letter:")).lower()
          if letter.isalpha() and len(letter)==1:
                if letter not in guessed_letters:
                       break
                else:
                   print("\n"+"It is already guessed.please enter again")
          else:
               print("\n"+"Invalid,print only alphabet and only one!")
        
        guessed_letters.append(letter)
        if letter not in word:
          print("\n"+f"{letter} not in word!"+"\n")
          lives-=1
        else:
            print("\n"+"The letter is correct.")
            for i in range(len(answer)):
               if answer[i]==letter:
                  display[i]=letter
        result = "".join(display)
        if result==word:
           print("\n"+"Conratulations,You Won!")
           break
    else:
        print("\n"+"You lost!")
        print("\n"+"The word was:", word)
while True:
   hangman()
   while True:
    again=input("\n"+"do you want to play again(yes/no):").lower()
    if again=="yes" :
       break
    elif again=="no":
       print("\n"+"Thank you for playing")
       exit()
    else:
       print("\n"+"please print yes or no.")