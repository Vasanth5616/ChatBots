from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('AdvancedChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

# Custom training data
trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

# Start the conversation
print("ChatBot: Hello! How can I assist you today?")

while True:
    user_input = input("User: ")

    # Break the loop if the user enters 'quit'
    if user_input.lower() == 'quit':
        break

    # Get a response from the chatbot
    response = chatbot.get_response(user_input)

    # Print the chatbot's response
    print("ChatBot:", response)
