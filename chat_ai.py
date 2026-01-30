# Simple AI Chat Application (Offline)

print(" AI Chat Application")
print("Type 'bye' to exit\n")

def ai_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking "

    elif "your name" in user_input:
        return "I am a simple AI Chatbot written in Python."

    elif "python" in user_input:
        return "Python is a great language for beginners and AI projects."

    elif "numpy" in user_input:
        return "NumPy is used for numerical computing in Python."

    elif "help" in user_input:
        return "Sure! You can ask me about Python, NumPy, or basic programming."

    elif "bye" in user_input:
        return "Goodbye! Have a great day "

    else:
        return "Sorry, I didn't understand that. Can you try again?"

# Chat loop
while True:
    user_message = input("You: ")

    reply = ai_response(user_message)
    print("AI:", reply)

    if user_message.lower() == "bye":
        break
