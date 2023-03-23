import telebot
import requests

API_KEY = "39f8c08e1fc23984d36e561deb783bd0"
bot = telebot.TeleBot("6254335635:AAFn5kGCwg8PFQPSiiPTaxJDg57uxMIFa9Y")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to Weather Bot\n. ادخل اسم المدينة للحصول على تفاصيل الطقس فيها.\n  ')

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        message_text = f'{description}.\n درجة الحرارة: {temperature}°C.\n    الحرارة المحسوسة: {feels_like}°C.\n    نسبة الرطوبة: {humidity}%. \n    الرياح: {wind_speed} m/s.\n'
        
        bot.reply_to(message, message_text)
    else:
        bot.reply_to(message, 'Sorry, I could not get weather information for this city. Please try again with another city name.')

bot.polling()
