import random
import string
while True:
 n=int(input("enter the length of password:"))
 if n<0 or n>21:
   print("please enter password size between 1 to 20")
 else:
   break

c=[str(random.randint(0,9)),random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.punctuation)]
h=[]
if n<4:
  while len(h)<n:
     a=random.choice(c)
     if a in h:
      continue
     h.append(a)
  for i in h:
   print(i,end="")
  
  
else:
 while len(c)<n:
    b=[str(random.randint(0,9)),random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.punctuation)]
    a=random.choice(b)
    c.append(a)
 random.shuffle(c)

 for i in c:
   print(i,end="")