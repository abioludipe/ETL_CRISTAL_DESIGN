import pandas as pd
import datetime as dt
import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


def transform(merged_data):

    """Perform necessay transformation including

    :param X: merged data 
    """

    try:
        merged_data['Date'] = pd.to_datetime(merged_data['Date'])

    except Exception as e:
        logging.error(f"Error: {{e}}")
    try:
        logging.info('Dropping columns')
        print('\n')
        merged_data.drop(['Unnamed: 0', 'index','MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'Type', 'Temperature', 'Size'], 
                         axis = 1, inplace = True, index = None)
        logging.info("Columns dropping done")
        print('\n')
    except Exception as e:
        logging.error(e)
        print('\n')
    
    try:
        logging.info('Filling null values')
        print('\n')
        merged_data = merged_data.fillna(value={"Date": merged_data['Date'].max(), 
                                            'Weekly_Sales': merged_data['Weekly_Sales'].mean(),
                                            'CPI': merged_data['CPI'].mean(),
                                            'Unemployment': merged_data['Unemployment'].mean()}, axis = 0)
        logging.info('Null filled successfully')
    except Exception as e:
        logging.error(e)

    try:
        merged_data['Month'] = merged_data['Date'].dt.month
        logging.info('Adding month column')
        print('\n')
    except Exception as e:
        logging.error(f"Error: {e}")
        print('\n')
    #filter rows with sales greater than 10,000

    try:
        logging.info('Filtering sales less than 10000')
        print('\n')
        clean_data = merged_data.loc[merged_data['Weekly_Sales'].astype(float) >= 10000.0, :]
    except Exception as e:
        logging.error(f'Error: {e}')
    
    return clean_data



