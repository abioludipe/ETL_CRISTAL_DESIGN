import pandas as pd
import datetime as dt
import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def avg_monthly_sales(clean_data):

    holiday_df = clean_data[['Weekly_Sales', 'Month']]
    
    agg_data = holiday_df.groupby(by=['Month']).mean()

    agg_data = agg_data.round({"Weekly_Sales": 2})

    return agg_data