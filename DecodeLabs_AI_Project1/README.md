# Rule-Based AI Chatbot 🤖

## DecodeLabs Artificial Intelligence Internship
### Project 1

## Project Overview

This project is a simple Rule-Based AI Chatbot developed as part of the DecodeLabs Artificial Intelligence Internship.

The chatbot responds to predefined user inputs using Python control flow and a dictionary-based knowledge base.

## Objective

The objective of this project is to create a chatbot that:

- Handles greetings
- Responds to predefined user inputs
- Runs continuously using a while loop
- Handles exit commands
- Provides a fallback response for unknown inputs

## Technologies Used

- Python 3
- Dictionaries
- If-else statements
- While loop
- String methods

## Features

- 👋 Greeting responses
- 💬 Basic conversation
- 🤖 Chatbot introduction
- ❓ Help response
- 🔄 Continuous conversation
- 🔡 Case-insensitive input
- 🧹 Whitespace handling
- ⚠️ Fallback response
- 🚪 Exit commands: `bye`, `exit`, `quit`

## How It Works

1. The chatbot takes input from the user.
2. The input is converted to lowercase.
3. Extra spaces are removed.
4. The chatbot checks the input against predefined responses.
5. It returns the matching response.
6. If there is no match, a fallback response is displayed.
7. The chatbot continues until the user enters an exit command.

## How to Run

Open the terminal in the project folder and run:

```bash
python chatbot.py