import pandas as pd
import datetime as dt
import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


# Create the validation() function with one parameter: file_path - to check whether the previous function was correctly executed
def validation(file_path):
  	# Use the "os" package to check whether a path exists
    file_exists = os.path.exists(file_path)
    # Raise an exception if the path doesn't exist, hence, if there is no file found on a given path
    if not file_exists:
        raise Exception(f"There is no file at the path {file_path}")