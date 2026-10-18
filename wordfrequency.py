import string
print("===== WORD FREQUENCY COUNTER =====")
str=input("enter the string:").lower()
for i in str:
    if i in string.punctuation():
        new_str=str.replace(i,"")
words=new_str.split(" ").strip()
print("Total words:",len(words))
freq={}
for i in words:
    freq[i]=freq.get(i,0)+1
print("Unique Words:",len(freq))
print("===FREQUENCY OF WORDS===")
for word,value in freq.items():
    print(word,":",value)