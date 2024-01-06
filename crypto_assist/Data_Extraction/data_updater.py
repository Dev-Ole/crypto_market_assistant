from request_social import check_social_data
from request_fearandgreed import fear_and_greed
from request_sentiment import sentimental_data
from request_binance import chart_data

def update_data():
    #Check and update chart data
    chart_data()

    #Check and update social data
    check_social_data()

    #Check and update fear and greed data
    fear_and_greed()

    #Check and update sentimental data
    sentimental_data()

    print('✅ All dataframes have been updated.')
update_data()
