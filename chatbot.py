print("Welcome to Chatbot!")
print("Created by: D Bramheswari")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How can I help you?")
    elif user == "how are you":
        print("Bot: I'm fine, thank you!")
    elif user == "what is your name":
        print("Bot: I'm your simple chatbot!")
    elif user == "bye":
        print("Bot: Goodbye! Created by D Bramheswari")
        break
    else:
        print("Bot: Sorry, I don't understand.")