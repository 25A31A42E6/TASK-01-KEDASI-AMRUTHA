# DecodeLabs - Artificial Intelligence
# Project 1: Rule-Based AI Chatbot

responses = {
    "hello": "Hello! 👋 How can I help you?",
    "hi": "Hi there! 😊 Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "your name": "I'm a Rule-Based AI Chatbot created for the DecodeLabs Project 1.",
    "what can you do": "I can respond to simple predefined questions and greetings.",
    "help": "You can greet me, ask my name, ask how I am, or ask what I can do.",
    "thank you": "You're welcome! 😊",
}

print("===================================")
print("      🤖 DECODELABS AI CHATBOT")
print("===================================")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print()

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a great day!")
        break

    if user_input in responses:
        print("Bot:", responses[user_input])
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")