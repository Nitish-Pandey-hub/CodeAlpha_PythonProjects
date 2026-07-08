def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    elif "name" in user_input:
        return "I'm a simple chatbot!"
    else:
        return "Sorry, I didn't understand that."


def chat():
    print("Chatbot: Hello! Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


if __name__ == "__main__":
    chat()