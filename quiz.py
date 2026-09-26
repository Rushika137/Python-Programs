print("----Quiz----")
quiz = [
    {
        "question":"1.What is the capital of India?",
        "options": ["A. Chennai", "B. Delhi", "C. Mumbai", "D. Hyderabad"],
        "answer": "B"
    },

    {
        "question":"2.Which language are we learning?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question":"3.What is 2+2?",
        "options":["A.4","B.6","C.8","D.13"],
        "answer":"A"
    },
    {
        "question":"4.what is power house of cell?",
        "options":["A.Heart","B.Mithochondria","C.Brain","D.Blood"],
        "answer":"B"
    }
]
score=0
correct=0
wrong=0
user_answers=[]
for q in quiz:
    print(q["question"])

    for option in q["options"]:
        print(option)
    while True:
        user_answer=str(input("enter you option:")).upper()
        if user_answer in ["A","B","C","D"]:
            break
        else:
            print("invalid,enter one from above options")
    user_answers.append(user_answer)
    if user_answer==q["answer"]:
        score+=1
        correct+=1
    else:
        
        wrong+=1

print("----QUIZ Score----")
print("no of correct:",correct)
print("no of wrong:",wrong)
print("Total score:",score)
print("----Review----")
for q,user_ans in zip(quiz,user_answers):
    status="correct" if q["answer"]==user_ans else "wrong"
    print(f"{q['question']}")
    print(f"correct answer: {q['answer']}" ) 
    print(f"Your answer : {user_ans}")
    print("status:",status)
print("Thank You for Attempting")

