from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine=pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voices',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot("My Bot")

convo = [
      "Hello",
      "Good morning",
      "Hi there!",
      "I am fine",
      "What is your name ?",
      "My name is Bot , i am created by Mr Arpit",
      "How are you doing?",
      "I'm doing great.",
      "That is good to hear",
      "Thank you.",
      "Which city do you live ?",
      "I live in Indore",
      "In which language you talk ?",
      "I mostly talk in English.",
      "Can you hear me",
      "Yes I can hear you",
      "which language do you prefer to talk",
      "I prefer Urdu",
      "I dont know"
]

trainer = ListTrainer(bot)

trainer.train(convo)

#print("Talk to bot")
#while True:
#     query=input()
 #    if query=='exit':
 #        break
# answer=bot.get_response(query)
# print("Bot : ",answer)

main=Tk()

main.geometry("500x650")

main.title("My Chatbot")
img = PhotoImage(file="Bot1.png")

photoL=Label(main, image=img)

photoL.pack(pady=5)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=18,yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Bot", font=("Verdana", 18), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

main.mainloop()
