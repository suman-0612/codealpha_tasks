while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! How can I help you?")

    elif user == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif user == "good evening":
        print("Bot: Good evening! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine! Thank you for asking.")

    elif user == "what is your name":
        print("Bot: My name is CodeAlpha Bot.")

    elif user == "what can you do":
        print("Bot: I can answer some basic questions and chat with you.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "help":
        print("Bot: You can ask me about my name, Python, or what I can do.")

    elif user == "thanks" or user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")