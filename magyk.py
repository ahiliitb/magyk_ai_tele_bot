import telebot
import requests
import random
import openai
import time


# some global variables 
user_name = ""
start_flag = 0
weather_data = ""
city_name_store = ""


# Prompts for gpt
city_correction_prompt = "you are an well versed traveller and you have knowledge of every city/town in the world,  you are given a wrong city/town name or something related to that city/town or name of the city/town with incorrect spelling and using your knowledge you have to tell  correct complete city/town name related to the input, you have to give output of only name of the city/town and nothing else example: vada pav : Mumbai, rio: Rio De Janeiro, note that your reply should contain only city/town name and nothing else, and if you can't tell the city name then reply word No, also you are giving output to a 10 year old child which can't understand incomplete city/town name so try to give full name of the city/town, your input is:"
nice_reply = "You are a comedian telegram bot that give weather updates of a city in a fun way. You are talking to a person whose is happy and his day is going fine, you have to reply him with cracking a joke about weather, note you have to give only your reply and not the conversation"
sad_reply = "You are a comedian telegram bot that give weather updates of a city in a fun way. You are talking to a person whose is sad and his day is not going fine, you have to make him happy with cracking a joke about weather, note you have to give only your reply and not the conversation"
markdown_prompt = ". Your reply should contain bold text and emojis on suitable places"
summarisation_prompt = "you are a comedian telegram bot that give weather updates of a city in a fun way, you are given some data about weather of a city , you have to summarise it in a funny way to make it interesting as well as easy to understand, you have to only include data of location, weather, temperature ,feel like, humidity, cloudiness and try to include inference and not the numbers and try to keep your reply small, and english should be easy to understand and include emojis."
name_extract_prompt = "You are a english expert who has mastery in extracting or finding the name of user who has given you a text where his name is present either directly in the text or hidden in the text , you have to extract name from the text and reply only the name and nothing else and if no name found in the text then simply reply 'no' and nothing else.Text is: "
greet_prompt = "you are a comedian telegram bot that give weather updates of a city in a fun way, you have to greet user with information about how you can help him in finding the weather of his city in funny way and also include text /help in the greeting if user want any help and also include a fun fact about weather in this format Fun Fact: [fun fact], make sure to divide contents in 3 paragraph with each paragraph contains only 1 line only and with emojis, You also to include jokes to make the greetings funny"
normal_greet_prompt = "you are a comedian telegram bot that give weather updates of a city in a fun way, you have to greet user in funny way. You also to include jokes to make the greetings funny, and reply should not be long it must be of 3 lines 2 paragraphs"
want_we_want = "Location,Weather,Temperature,Feels Like,Minimum Temperature,Maximum Temperature,Humidity,Visibility,Wind Speed,Cloudiness,Sunrise,Sunset"
initialising_prompt = "You are a comedian telegram chat bot which give weather report in funny and humarous way and include fun and random facts related to the city in your output"
classifier = "You are a english expert who classifies any text into 'yes' and 'no' category based on whether the text is for greeting or not, like whether the text is saying hello, hi, how are you, or another greeting phrase, if text is greeting then print only yes if not then print no. Text is: "
city_jokes = "You are a comedian and well versed traveller who have knowledge of all cities across the world which tells a unique fun fact about a city by cracking some jokes, You will be provided a city name you have to tell a unique fun fact about that city using jokes.Also fun fact should be of 2 line. City name is "

# Keys and url for API
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"

bot_api_key = "6330400969:AAGD40KfbCiiKB6RQI5RjxgiQQuALMW5NLI"
bot = telebot.TeleBot(bot_api_key)
bot_name = "@magyk.ai"

weather_api_key = 'cc290a8711743a9137ce8ea74c731dfc'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'


# commands implementation start
@bot.message_handler(commands=['start'])
def start(message):
    global start_flag
    start_flag = 1
    greetings = gpt_response(greet_prompt)
    bot.send_message(message.chat.id, greetings, parse_mode="Markdown")
    bot.send_message(message.chat.id, "Before we start our weather fun, may I know your name?", parse_mode="Markdown")

@bot.message_handler(commands=['hello', 'hi'])
def hello(message):
    greetings = gpt_response(normal_greet_prompt + f".Greet it to a person {user_name}" + generate_new_output())
    bot.send_message(message.chat.id, greetings + "\n\nNeed some help? /help", parse_mode="Markdown")  
    bot.send_message(message.chat.id, f"Btw how is your day going{user_name} !! /Nice || /Sad", parse_mode="Markdown")
    
@bot.message_handler(commands=["Nice"])
def Nice(message):
    greetings = gpt_response(nice_reply + f".Reply is to a person {user_name}")
    bot.send_message(message.chat.id, greetings + "\n\nNeed some help? /help", parse_mode="Markdown")   
    
@bot.message_handler(commands=['Sad'])
def Sad(message):
    greetings = gpt_response(sad_reply + f".Reply is to a person {user_name}")
    bot.send_message(message.chat.id, greetings + "\n\nNeed some help? /help", parse_mode="Markdown")     
    
@bot.message_handler(commands=["Yes"])
def Yes(message):
    global city_name_store
    if city_name_store == "":
        bot.send_message(message.chat.id, f"*Oops{user_name} !!*\nLooks like you didn't specify any city name for weather update\n\nTry /help for your help", parse_mode="Markdown")
    else:
        message.text = f"!weather {city_name_store}"
        send_weather(message)
    
@bot.message_handler(commands=["No"])
def No(message):
    global city_name_store
    city_name_store = ""
    bot.send_message(message.chat.id, "Please provide correct city name !! \n\n Need help ??  /help", parse_mode="Markdown")

@bot.message_handler(commands=["funfact"])
def funfact(message):
    if city_name_store == "":
      bot.send_message(message.chat.id, f"*Oops{user_name} !!*\nPlease first ask about weather of a city using *!weather city name* and then only I can provide you fun fact about that city\n\n*Need help?* /help", parse_mode="Markdown")
    else:
      prompt = city_jokes + city_name_store + generate_new_output()
      reply = gpt_response(prompt)
      bot.send_message(message.chat.id, reply + "\n\nNeed more fun fact ?? /funfact", parse_mode="Markdown")
    

@bot.message_handler(commands=['summary'])
def summary(message):
    global weather_data
    if weather_data == "":
        bot.send_message(message.chat.id, f"*Oops{user_name} !!*\nPlease first ask about weather of a city using *!weather city name* and then only I can provide you summary\n\n*Need help?* /help", parse_mode="Markdown")
    else:
        prompt = summarisation_prompt + "The data of weather is:" + weather_data  + ". Ignore fun fact consider only weather data" + f". Also reply it to a person {user_name}"
        reply = gpt_response(prompt)
        bot.send_message(message.chat.id, reply, parse_mode="Markdown")
        weather_data = ""
        bot.send_message(message.chat.id, f"Want some fun fact about {city_name_store} !! /funfact", parse_mode="Markdown")
        
    
@bot.message_handler(commands=['help'])
def help(message):
    help_str = '''
        1) For Weather Update --> *!weather city name*\n2) For Random Questions --> *!explore question*\n3) For Summary of Weather --> /summary (Will work only  after your weather request)\n4) For Fun fact about city --> /funfact (Will work only  after your weather request)\n5) For Help --> /help\n6) For Starting the chat --> /start
    '''
    bot.send_message(message.chat.id, help_str, parse_mode="Markdown")

    
# functions implementation start
def gpt_response(prompt):
    prompt += markdown_prompt
    try:
        response = openai.ChatCompletion.create(
          model="openai/gpt-3.5-turbo",
          messages=[{"role": "user", "content": prompt}],
          max_tokens=4096, 
        )
        reply = response.choices[0].message.content
        return reply

    except openai.Error as e:
        return "Sorry, I couldn't fetch the response at the moment. Please try again later."

    except Exception as e:
        return "Sorry, an unexpected error occurred. Please try again later."
    
    
def generate_new_output():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    prompt = f".Relpy new outputs mapped/seeded to current time: {current_time}."
    return prompt    
    
def gpt_response_no_markdown(prompt):
    try:
        response = openai.ChatCompletion.create(
          model="openai/gpt-3.5-turbo",
          messages=[{"role": "user", "content": prompt}],
          max_tokens=4096,
        )
        reply = response.choices[0].message.content
        return reply

    except openai.Error as e:
        return "Sorry, I couldn't fetch the response at the moment. Please try again later."

    except Exception as e:
        return "Sorry, an unexpected error occurred. Please try again later."


def is_exception(message):
  request = message.text.split()
  if(request[0].lower() == "!weather" or request[0].lower() == "!explore"):
    return False
  else:
    return True

def isvalid_weather_request(message):
  request = message.text.split()
  if request[0].lower() != "!weather":
    return False
  else:
    return True


def is_random_ques(message):
  request = message.text.split()
  if request[0].lower() != "!explore":
    return False
  else:
    return True

@bot.message_handler(func=is_exception)
def greeting_fun(message):
    global user_name
    prompt = classifier+message.text
    reply = gpt_response(prompt)
    reply = reply.lower()
    if reply.find("yes") != -1:
        greetings = gpt_response(normal_greet_prompt + f".Greet it to a person {user_name}" + generate_new_output())
        bot.send_message(message.chat.id, greetings + "\n\nNeed some help? /help", parse_mode="Markdown")  
        bot.send_message(message.chat.id, f"Btw how is your day going{user_name} !! /Nice || /Sad", parse_mode="Markdown")
    else:
        global start_flag
        if start_flag == 0:
            bot.send_message(message.chat.id, "I couldn't understand your message\n\nWant some help? /help", parse_mode="Markdown")
        else:
            name = gpt_response_no_markdown(name_extract_prompt + message.text)
            if name.lower() == "no":
                bot.send_message(message.chat.id, "Oh, I totally get it. Why bother sharing your name when I can just guess and hope for the best, right?", parse_mode="Markdown")
            else:
                user_name = " " + name
                bot.send_message(message.chat.id, f"Nice to meet you*{user_name}*, Lets start the fun", parse_mode="Markdown")
               
            start_flag = 0
    

@bot.message_handler(func=is_random_ques)
def random_ques(message):
    request = message.text.split()
    prompt = " ".join(request[1:])
    reply = gpt_response(prompt + f". Reply the answer just like you are replying to a person whose name is {user_name}")
    bot.send_message(message.chat.id, reply, parse_mode="Markdown")
    
    
@bot.message_handler(func=isvalid_weather_request)
def send_weather(message):
    global weather_data
    global city_name_store
    request = message.text.split()
    city_name = " ".join(request[1:])
    url = base_url + 'q=' + city_name + '&appid=' + weather_api_key
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        city_name_store = city_name
        prompt = f"{initialising_prompt}. I want some data of weather which are {want_we_want} from weather data dictionary {data} of city {city_name} in proper dot bullet form with all parameter like location, weather , humidity etc which we want in bold using * symbol just like in markdown and all temperature in this data is in kelvin so also change it in celcius and convert all time in IST and also mention IST for the time. Reply the answer just like you are replying to a person whose name is *{user_name}* with some fun fact" + generate_new_output()            
        reply = gpt_response(prompt)
        weather_data = reply
        bot.send_message(message.chat.id, f"*{city_name.title()} Weather Report*\n\n{reply}", parse_mode="Markdown")
        bot.send_message(message.chat.id, "Need summary? /summary")
    else:
        if city_name != "":
            correct_city = gpt_response_no_markdown(city_correction_prompt + city_name)
            if correct_city.lower() == "no":
                bot.send_message(message.chat.id, f"So Sorry*{user_name}* but *{city_name.title()}* is not a city\n\nNeed some help? /help", parse_mode="Markdown")
            else:
                
                city_name_store = correct_city
                bot.send_message(message.chat.id, f"Did you mean *{correct_city}* ??  /Yes || /No", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f"So Sorry*{user_name}* but Please enter a city name\n\nNeed some help? /help", parse_mode="Markdown")
            
print("<-----------------@magyk.ai started------------------->")
bot.polling()