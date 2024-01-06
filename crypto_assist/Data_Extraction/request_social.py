import requests
import pandas as pd
from datetime import datetime, timedelta
import os

#import API Key .envrc
import os
from dotenv import load_dotenv
load_dotenv()
api_key_social = os.getenv("API_KEY_SOCIAL")

def check_social_data():
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

    def days_to_fetch(start=date_object_today, final=date_object_last_date):
        if start == final:
            return start
        else:
            return (start - final).days


    def date_check(days_to_fetch=days_to_fetch(), date_object_today=date_object_today):
        if days_to_fetch == date_object_today:
            print("✅ Social numbers dataframe is up to date.")
            return
        else:
            print(f'Date frame incomplete fetching {days_to_fetch}')
            #First make a request to cryptocompare API to get the social stats
            url= f'https://min-api.cryptocompare.com/data/social/coin/histo/day?&coinId=7605&limit={days_to_fetch}&api_key={api_key_social}'
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
            df = df.drop(0)
            df = df.reset_index(drop=True)
            #Now convert the date column to datetime year month day
            df['date'] = df['date'].apply(lambda timestamp: datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d'))

            #Finally save the resulting dataframe to a file
            print('✅The new data has been successfully extracted and the new dataframe to be added is below.')

            df.to_csv((os.path.join(route_path, 'raw_data','social_number_data.csv')), mode='a', header=False, index=False)
    date_check()