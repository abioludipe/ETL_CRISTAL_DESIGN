import pandas as pd
import datetime as dt
import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def load(clean_data, agg_data):
    if os.path.exists('./clean_data.csv'):
        pass
    else:
        clean_data.to_csv('./clean_data.csv', index = False)
        return clean_data

    if os.path.exists('./agg_data.csv'):
        pass
    else:
        agg_data.to_csv('./agg_data.csv', index = False)
        print('Data loaded successfully')
        return agg_data
    
    