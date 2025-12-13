#RULE BASED CHAT ASSISTANT


import datetime
import time

presentHour=datetime.datetime.now().hour
name=input("Enter your name:")
if 5<=presentHour<=11:
    print("Good Morning!",name)
elif 12<=presentHour<=16:
    print("Good Afternoon!",name)
elif 17<=presentHour<=20:
    print("Good Evening!",name)
else:
    print("Good Night!",name)

print("Welcome to Rule-based chat assistant!")
print("You can ask me basic question and type 'exit' to quit")


               #CHABOT MEMORY CREATION
responses={
    "hi":"Hello! How can I assist you?",
    "how are you?":"I'm just a program, but thanks for asking!",
    "what is your name?":"I am a Rule-based Chat Assistant.",
    "motivate me":"Believe in yourself! You can achieve great things with determination and hard work.",
    "happy":"Happiness is a choice. Choose to be happy and spread positivity around you.",
    "functin":"Functions are reusable blocks of code that perform a specific task.",
     "exit":"Goodbye! Have a great day!"
}

#FUNCTION TO GET RESPONSE 
def getResponseOfBot(userQuery):
    userQuery=userQuery.lower()
    for eachkey in responses:
        if eachkey in userQuery:
            return responses[eachkey]
    return "I'm sorry, I don't understand your question."


#USER INPUT

while True:
      userInput=input("Pleases ask your question:")
      reply=getResponseOfBot(userInput)
      print("Bot:",reply)

      if "exit" in userInput.lower():
           break
      