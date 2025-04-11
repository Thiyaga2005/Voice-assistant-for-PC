import requests
import pywhatkit as kit


def search_on_google(query):
    kit.search(query)


def youtube(video):
    kit.playonyt(video)


def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey"
                          f"=984ca9e123dd40389c4f95fdcaa15196").json()
    articles = result["articles"]
    for articles in articles:
        news_headline.append(articles["title"])
    return news_headline[:6]


def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address["ip"]


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def weather_forecast(city):
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3753473e0e2758e52388dc88b39fe154"
    ).json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}℃", f"{feels_like}℃"


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
