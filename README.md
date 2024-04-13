# Magyk AI TeleBot (@magyk.ai)

## Set up to run the TeleBot
- Code is present inside Google Colab Notebook, so just open `telegram_bot_code.ipynb` file.
- Click on `open in colab` to open the colab notebook and then run both cells.
- Go to telegram and open `magyk.ai`.

## ChatGPT chat link
`https://chat.openai.com/share/c86ad2de-482c-4838-b8a2-bab66dfebdce`

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
- Stored prompts in global variables and each time command is called, the prompt is passed into GPT 3.5 API
- Interaction with the ChatGPT API is used for generating responses, greetings, and random fun facts.

### Usage
1. Start the chat by sending the /start command.
2. When prompted, provide your name. The bot will verify the name and greet you accordingly.
3. Enjoy chatting with the bot and explore the weather-related fun facts it has to offer!

## /hi or /hello or normal hi, hello, etc. Command

### Overview
The `/hi` or `/hello` command, as well as normal greetings like "hi" or "hello," is used to greet the user. If the user's name has been provided before, the bot will greet the user by name; otherwise, it will greet the user without a name. Additionally, for normal greetings and other text like "how are you" or "bye," the bot will check if the text is a greeting. If it is a greeting, the bot will greet the user; otherwise, it will indicate that the message can't be understood.

### Mood Inquiry
After greeting the user, the bot will ask a question about the user's mood. If the user's mood is nice, the bot will reply in a funny way, greeting the user with a joke. If the user's mood is not nice, the bot will console the user with a joke about the weather.

### Implementation Details
- Stored prompts in global variables and each time command is called, the prompt is passed into GPT 3.5 API
- Interaction with the ChatGPT API is used for generating responses, greetings, and jokes.

### Usage
1. Send a greeting message such as "/hi," "/hello," or "hi" to start the interaction.
2. If you haven't provided your name before, the bot will greet you without a name.
3. Enjoy chatting with the bot and explore the jokes and greetings it has to offer!

## !weather Command

### Overview
The `!weather` command is used to provide weather updates for a specific city. It also includes a fun fact about that city and asks for a summary. If the city name is given incorrectly, the bot will attempt to predict the correct city name and confirm with the user. If the predicted city name is correct, it will provide the weather for that city; otherwise, it will reply with "city not found." The city name and weather data are stored in global variables for use in the summary function. Weather updates are provided using the OpenWeatherMap API, and the prediction of city names and random fun facts are done using suitable prompts and the ChatGPT API.

### Implementation Details
- Uses the OpenWeatherMap API for weather updates.
- Stored prompts in global variables and each time command is called, the prompt is passed into GPT 3.5 API
- Interaction with the ChatGPT API is used for predicting city names and providing fun facts.

### Usage
1. Send a message in the format "!weather city name" to get the weather update for that city.
2. If the city name is incorrect, the bot will attempt to predict the correct city name.
3. Confirm the predicted city name if it is correct, and the bot will provide the weather update for that city.
4. Enjoy the fun fact about the city and provide a summary if prompted.

## /help Command

### Overview
The `/help` command is used to provide users with information about all available commands, their uses, and the format in which they should be used.

### Functionality
- Provides a list of all available commands.
- Describes the purpose of each command.
- Specifies the format in which each command should be used.

### Usage
1. Send the `/help` command to the bot.
2. The bot will respond with a list of available commands and their descriptions.
3. Use this information to understand how to interact with the bot and make the most of its features.

## /summary Command

### Overview
The `/summary` command is used to provide a summary of the weather report for a city that was requested earlier. This command only works if the weather report for a specific city has been requested just before using the summary command. The summary is generated using suitable prompts and the ChatGPT API.

### Functionality
- Provides a summary of the weather report for a city that was requested earlier.
- Requires that the weather report for the city was requested just before using the summary command.

### Usage
1. Request the weather report for a city using the appropriate command.
2. After receiving the weather report, use the `/summary` command to get a summary of the report.
3. The bot will respond with a summary based on the weather report for the city.

## !explore Command

### Overview
The `!explore` command is used to reply with the answer to a random question asked by the user in a funny way. This is achieved by using suitable prompts and the ChatGPT API to generate a humorous response.

### Functionality
- Replies with the answer to a random question asked by the user.
- Provides the answer in a funny and engaging way.

### Usage
1. Ask a random question.
2. Use the `!explore` command to get a funny response with the answer to the question.
3. Enjoy the humorous and engaging interaction with the bot!




