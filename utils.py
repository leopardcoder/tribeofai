import main, os, json
from datetime import datetime
from preparation_data import *
from calendar import monthrange

binance_products = []
period_days_array = [] # hungarian notations...

def read_info_file(file_name): # should have concrete functionality to little to make a function.
    with open(file_name, 'r') as file:
        print(file.read()) # printing is a side effect.

def read_from_file(file_name, array): # read from json file naming should be.
    with open(file_name, 'r') as file:
        for line in file:
            array.append(json.loads(line))

def get_today_date():
    now = datetime.now()
    return now.strftime("%Y_%m_%d")

def get_today_date_zenbot_format():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M")

def create_dir(crypto_pair):
    dir_name = os.getcwd() + '/simulations/' + crypto_pair
    try:
        os.makedirs(dir_name)
        print("Directory " , dir_name ,  " Created ")
    except FileExistsError:
        print("Directory " , dir_name ,  " already exists")

def get_days_of_month(date): # if unused function to create  a new branch, not commit.
    year = str(date)[0:4] # use git more often.
    month = str(date)[slice(4,6)]
    num_days = monthrange(int(year), int(month))[1]
    for x in range(1, num_days):
        if x >= 10:
            period_days_array.append(str(date) + str(x))
        else:
            period_days_array.append(str(date) + str(0) + str(x))

def get_period_months(period):
    start_date = period.split('-')[0] # google variable unpacking more beautiful way
    end_date = period.split('-')[1]

    for x in range(int(start_date), int(end_date)+1):
        get_days_of_month(x)
