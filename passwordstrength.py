import string
common_passwords = {
    "123456",
    "12345678",
    "123456789",
    "12345",
    "1234567890",
    "password",
    "password123",
    "admin",
    "admin123",
    "qwerty",
    "qwerty123",
    "abc123",
    "iloveyou",
    "welcome",
    "welcome123",
    "letmein",
    "monkey",
    "dragon",
    "football",
    "princess",
    "sunshine",
    "master",
    "login",
    "passw0rd",
    "Password",
}
suggestions=[]
password=input("enter the password:")
n=len(password)
if n == 0:
    print("Password cannot be empty!")
else:
    if password.lower() in common_passwords:
      print("This is a common password. Choose a less predictable one.")
      exit()
# Detect predictable patterns
patterns = [
    "123", "234", "345", "456", "567",
    "678", "789", "abc", "bcd", "cde",
    "def", "qwerty", "asdf", "zxcv"
]

for pattern in patterns:
    if pattern in password.lower():
        suggestions.append(
            f"Your password contains a predictable pattern: '{pattern}'."
        )
score=0
uppercase=0
lowercase=0
punctuation=0
digit=0
freq={}
for i in password:
     freq[i]=freq.get(i,0)+1
if len(freq) == 1:
        suggestions.append(
            "All characters are identical. Choose a different password."
        )
for i in freq:
 if freq[i]>=n/3 and freq[i]<n:
     suggestions.append(f"{i} character repeated {freq[i]}!")

if n>=8 and n<=15:
    score+=1
else:
     print("please choose password length from 8 to 15.")
for i in password:
    if i.islower() :
        lowercase+=1
    elif i.isupper():
        uppercase+=1
    elif i in string.punctuation:
         punctuation+=1
    elif i.isdigit():
                digit+=1
         
if uppercase>=1:
    score+=1
else:
     suggestions.append ("please add some uppercase")
if lowercase>=1:
    score+=1
else:
    suggestions.append ("please add some lowercase")
if digit>=1:
     score+=1
else:
     suggestions.append ("please add some digits")
if punctuation>=1:
    score+=1
else:
    suggestions.append ("Add a special character.")
print("the score of password is:",score,"/5")
if score<=1:
     print("password level:Poor!")
elif score<=3:
     print("password level:medium!")
elif score<=5:
     print("password level:strong")
if len(suggestions)==0:
    print("\nAll selected checks passed!")
else:
 print("suggestions to make it stronger password!")
 for i in suggestions:
   print("-",i)


