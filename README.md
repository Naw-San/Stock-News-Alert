# Stock-News-Alert

# Overview
  The program monitors your favorite stock prices and send notification with the latest news articles to your phone.
  The program specifically monitors Tesla Inc(TSLA) stock prices changes by 1% between yesterday and the day before yesterday closing prices.

# Features
1) Stock Monitoring
   Retrieve daily stock prices for Tesla using Alpha Vantage API (https://www.alphavantage.co/query)
   
2) News Updates
   Fetch the latest Tesla-related using the News API (https://newsapi.org/v2/everything)

3) SMS/WhatsApp Notifications
   Send SMS or WhatsApp messages with top news headlines using the Twilio API (Your own Twilio Account SID and Auth Token)

# Tools/Technologies
  Python, with external requests and twilio Client libraries, was solely used for this program.

# Prerequisites
  - Python 3.6 or later installed on your system; Windows, MacOS, or Linux
  - Install requests and Twilio Client module libraries on your system. (Please refer to this -> https://www.python.org/)
  - An account with:
      Alpha Vantage
      NewsAPI
      Twilio for Twilio account SID and Auth Token
  - Install python-dotenv in your terminal
      pip install python-dotenv
  - Then create .env(enviornment variables) file in your project directory

  # Usage
  You can follow your favorite stock news. Please refer to this -> www.alphavantage.co for stock symbol and company name.
    For example, stock symbol for Tesla is TSLA and Tesla company name is Tesla Inc.

  And you need to generate your own Twilio Account SID and Auth Token from Twilio website https://www.twilio.com/
  Replace your SID and Auth Token on line 13 and line 14 in the main.py file 

# Run the program
  When you have your favorite STOCK, COMPANY_NAME, SID, and Auth Token, run your progrm on your system. Below is the command to run the program,
    
    python3 main.py TSLA "Tesla Inc"

# Run the program in the Cloud
  You can schedule and run the program everyday on www.pythonanywhere.com.
  It's free, you just need to sign up!



