from datetime import datetime, date

print("=" * 40)
print("🤖 Welcome to Python ChatBot")
print("Type 'help' to see commands.")
print("Type 'bye' to exit.")
print("=" * 40)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi":
        print("ChatBot: Hello! How are you?")

    elif user == "how are you":
        print("ChatBot: I am fine. Thank you!")

    elif user == "good morning":
        print("ChatBot: Good Morning! Have a wonderful day!")

    elif user == "good afternoon":
        print("ChatBot: Good Afternoon!")

    elif user == "good evening":
        print("ChatBot: Good Evening!")

    elif user == "good night":
        print("ChatBot: Good Night! Sweet dreams!")

    elif user == "what is your name":
        print("ChatBot: My name is Python ChatBot.")

    elif user == "who are you":
        print("ChatBot: I am a chatbot created using Python.")

    elif user == "who created you":
        print("ChatBot: I was created by a Python programmer.")

    elif user == "where are you":
        print("ChatBot: I am running inside your computer.")

    elif user == "how old are you":
        print("ChatBot: I don't have an age.")

    elif user == "what can you do":
        print("ChatBot: I can answer simple questions and chat with you.")

    elif user == "python":
        print("ChatBot: Python is a popular programming language.")

    elif user == "ai":
        print("ChatBot: AI stands for Artificial Intelligence.")

    elif user == "machine learning":
        print("ChatBot: Machine Learning is a branch of AI.")

    elif user == "deep learning":
        print("ChatBot: Deep Learning uses neural networks to learn from data.")

    elif user == "date":
        print("ChatBot: Today's date is", date.today())

    elif user == "time":
        print("ChatBot: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif user == "tell me a joke":
        print("ChatBot: Why do programmers hate nature? It has too many bugs!")

    elif user == "motivate me":
        print("ChatBot: Believe in yourself. Success comes through hard work!")

    elif user == "quote":
        print("ChatBot: Learning never exhausts the mind.")

    elif user == "study tips":
        print("ChatBot: Study daily, revise often, and practice coding.")

    elif user == "exam tips":
        print("ChatBot: Stay calm, manage your time, and read questions carefully.")

    elif user == "your favorite color":
        print("ChatBot: My favorite color is Blue.")

    elif user == "your favorite food":
        print("ChatBot: I don't eat food, but pizza sounds delicious!")

    elif user == "weather":
        print("ChatBot: Sorry, I cannot check live weather.")

    elif user == "thank you":
        print("ChatBot: You're welcome!")

    elif user == "help":
        print("\nAvailable Commands:")
        print("hello, hi")
        print("how are you")
        print("good morning")
        print("good afternoon")
        print("good evening")
        print("good night")
        print("what is your name")
        print("who are you")
        print("who created you")
        print("where are you")
        print("how old are you")
        print("what can you do")
        print("python")
        print("ai")
        print("machine learning")
        print("deep learning")
        print("date")
        print("time")
        print("tell me a joke")
        print("motivate me")
        print("quote")
        print("study tips")
        print("exam tips")
        print("your favorite color")
        print("your favorite food")
        print("weather")
        print("thank you")
        print("bye")

    elif user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot: Sorry, I don't understand that command.")
