import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_API_KEY = "82YNUCY01M9S2U4T"
news_apikey = "fd37049e064f42af81a21eaec68e506f"
TWILIO_acc_sid = "ACca06ad31bbd29b51f2ae9f97d3457e7a"
TWILIO_AUTH_TOKEN = "a2fd50358607e78fd2228bfaf65f58c0"
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : stock_API_KEY
}

stock_response = requests.get(url= STOCK_ENDPOINT, params= stock_params)
stock_data = stock_response.json()
stock_slice = stock_data["Time Series (Daily)"]
# now converting the dictionary into a list by using list comprehension.
# list = [new item for item in list]
data_list = [values for (key,values) in stock_slice.items()]
yesterday_data = data_list[0]
yesterday_price = yesterday_data["4. close"]

df_yesterday_data = data_list[1]
df_yesterday_price= df_yesterday_data["4. close"]

difference = abs(float(yesterday_price) - float(df_yesterday_price))


diff_percent = (difference / float(yesterday_price)) * 100

    

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

if diff_percent > 5:
    news_params = {
        "apiKey" : news_apikey,
        "qInTitle" : COMPANY_NAME
    }
    news_response = requests.get(url = NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    




## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
# lets convert the dictionary into list by using list comprehension

formatted_articles = [f"Headlines:{article['title']}. \nBrief: {article['description']}" for article in three_articles]
client = Client(TWILIO_acc_sid, TWILIO_AUTH_TOKEN)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+13155574770",
        to="+917339440825"

    )
 
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

