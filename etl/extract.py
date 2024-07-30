import pandas as pd
import datetime as dt
import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# Extract function takes the sales_data and extra information to be merged
def extract(sales_data, extra_data):
    """Extract the grocery data and merged it with extra information about the stores

    :param X: sales information
    :param Y: extra information about the store

    :return: merged_data

    """
    try:
        grocery_sales = pd.read_csv(sales_data)
        logging.info(f"{sales_data} loaded successfully")
        print('\n')
    except Exception as e:
        logging.error(f"{e}: {sales_data} cannot be found in the path")
        print('\n')
    try:
        extra_info = pd.read_parquet(extra_data)
        logging.info(f"{extra_data} loaded successfully")
        print('\n')
    except Exception as e:
        logging.error(f"{e}: {extra_data} not foundd in the path")
        print('\n')
    merged_df = grocery_sales.merge(extra_info, on = 'index')
    logging.info("Extraction Completed")
    print('\n')
    return merged_df

