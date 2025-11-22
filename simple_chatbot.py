def chatbot():
    print("Chatbot: Hello! I am your simple chatbot.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks!")

        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that.")


# Run the chatbot
chatbot()
