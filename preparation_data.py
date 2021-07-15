import main
import glob, subprocess, json, re, shutil
from utils import *

sim_files_list = glob.glob("/home/linas/zenbot/simulations/*")
strategies_dir_list = glob.glob("/home/linas/zenbot/extensions/strategies/*/")
strategies = []
binance_products = []
json_binance_products = []
binance_selectors = []

def get_strategy_names():
    for strategy_name in strategies_dir_list:
    	strategies.append(strategy_name.split("/")[-2])

def get_binance_selector():
    read_from_file('visi_Produktai.txt', binance_products, 'binance')
    for x in binance_products:
    	json_binance_products.append(json.loads(x.replace("'", "\"")))
    for y in json_binance_products:
    	binance_selectors.append(y['exchange'] + '.' + y['asset'] + '-' + y['currency'])

def check_if_crypto_pair_exists(crypto_pair):
    for x in binance_selectors:
        if x.endswith(crypto_pair) == True:
            print("Crypto pair found...")
            return
    exit()
