import requests
import numpy as np
import pandas as pd
import time
from datetime import datetime
import os

#This defines the current day
today = datetime.now().strftime("%Y-%m-%d")

date_format = '%Y-%m-%d'

# Convert the string to a datetime object
date_object_today = datetime.strptime(today, date_format)

#Now collect the last date in the csv_file social_number_data
route_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

df_social = pd.read_csv(os.path.join(route_path, 'raw_data','social_number_data.csv'))

last_date = df_social['date'].iloc[-1]

#Convert this last date into a date
date_object_last_date = datetime.strptime(last_date, date_format)

days_to_fetch = (date_object_today - date_object_last_date).days

print(date_object_last_date)

print(days_to_fetch)


'''def date_check():
    if days_to_fetch == 0:
        print("✅ Social numbers dataframe is up to date.")
        return
    else:
        print(f'Date frame incomplete fetching {days_to_fetch}')
        #First make a request to cryptocompare API to get the social stats
        url= f'https://min-api.cryptocompare.com/data/social/coin/histo/day?&coinId=7605&limit={days_to_fetch}&api_key=ec6ccfef0683ed17b8dea49e01c0954abcd030ba0dd27eb704d1c829dead85e6'
        r = requests.get(url)
        data = r.json()

        #Now filter through the json response and convert it to a list
        Data = []
        for i in range(0,len(data['Data'])):
            Data.append(data['Data'][i])

        #Now filter through the list and extract the chosen values
        updated_data = []
        for i in range(0,len(Data)):
            updated_data.append((Data[i]['time'],Data[i]['twitter_followers'],Data[i]['twitter_favourites'],Data[i]['reddit_subscribers'],Data[i]['reddit_active_users'],Data[i]['reddit_comments_per_day']))

        #Now create a dataframe for the data
        df = pd.DataFrame(updated_data)
        df.columns=['date','twitter_followers','twitter_favourites','reddit_subscribers','reddit_active_users','reddit_comments_per_day']

        #Now convert the date column to datetime year month day
        df['date'] = df['date'].apply(lambda timestamp: datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d'))

        #Finally save the resulting dataframe to a file
        df.to_csv('social_number_data.csv', index=False)
'''


'''
#First make a request to cryptocompare API to get the social stats
url= 'https://min-api.cryptocompare.com/data/social/coin/histo/day?&coinId=7605&limit=2000&api_key=ec6ccfef0683ed17b8dea49e01c0954abcd030ba0dd27eb704d1c829dead85e6'
r = requests.get(url)
data = r.json()

#Now filter through the json response and convert it to a list
Data = []
for i in range(0,len(data['Data'])):
    Data.append(data['Data'][i])

#Now filter through the list and extract the chosen values
updated_data = []
for i in range(0,len(Data)):
    updated_data.append((Data[i]['time'],Data[i]['twitter_followers'],Data[i]['twitter_favourites'],Data[i]['reddit_subscribers'],Data[i]['reddit_active_users'],Data[i]['reddit_comments_per_day']))

#Now create a dataframe for the data
df = pd.DataFrame(updated_data)
df.columns=['date','twitter_followers','twitter_favourites','reddit_subscribers','reddit_active_users','reddit_comments_per_day']

#Now convert the date column to datetime year month day
df['date'] = df['date'].apply(lambda timestamp: datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d'))

#Finally save the resulting dataframe to a file
df.to_csv('social_number_data.csv', index=False)'''
