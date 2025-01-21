import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "647563f29bc9426fbbe0bc060714560f"
STOCK_API_KEY = "XRO8LKKWIXGEWBMI"

#twilio
account_sid = "ADD YOUR ACCOUNT ID HERE"
auth_token = "ADD YOUR TOKEN HERE"


stock_parameter = {
    "function" : "TIME_SERIES_DAILY",
    "apikey" : STOCK_API_KEY,
    "symbol" : STOCK,
}
response = requests.get(url=STOCK_ENDPOINT,params=stock_parameter)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_close = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_close = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_close) - float(day_before_yesterday_close))
diff_percentage = (difference / float(yesterday_close)) * 100


news_parameter = {
    "qInTitle" : COMPANY_NAME,
    "apiKey" : NEWS_API_KEY,
    "language" : "en",
}
if diff_percentage > 1:
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameter)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    for item in formatted_articles:
        message = client.messages.create(
            from_="whatsapp:+14152222222", #<- ADD WHATSAPP NUMBER
            body=item,
            to="whatsapp:+14150000000"  #<- ADD YOUR NUMBER HERE
        )









