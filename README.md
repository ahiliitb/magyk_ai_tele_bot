# magyk_ai_tele_bot

## /start Command

### Overview
The `/start` command is used to initialize the chat with the Weather Bot. It greets the user with a random fun fact about the weather and prompts the user to provide their name.

### Functionality
1. **Greeting**: The command greets the user with a random fun fact about the weather.
2. **Name Prompt**: It asks the user to provide their name.
3. **Name Verification**: After the user provides their name, the command checks if the name is logical. If the name is valid, it greets the user by name. If not, it responds with a message indicating that it's okay if the user doesn't want to provide their name.

### Global Variable
The user's name is saved in a global variable for further use.

### Implementation Details
- The command is implemented in Python using the telebot library.
- Interaction with the ChatGPT API is used for generating responses, greetings, and random fun facts.

### Usage
1. Start the chat by sending the /start command.
2. When prompted, provide your name. The bot will verify the name and greet you accordingly.
3. Enjoy chatting with the bot and explore the weather-related fun facts it has to offer!

