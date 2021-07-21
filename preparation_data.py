import main
import glob, subprocess, json, re, shutil, os
from utils import *

sim_files_list = glob.glob(os.getcwd() + "/simulations/*")
strategies_dir_list = glob.glob(os.getcwd() + "/extensions/strategies/*/")
strategies = []
binance_products = []
json_binance_products = []
binance_selectors = []
exchange = 'binance'
all_products = 'visi_Produktai.json'

def get_strategy_names():
    print(sim_files_list, strategies_dir_list)
    for strategy_name in strategies_dir_list:
    	strategies.append(strategy_name.split("/")[-2])

def get_binance_selector():
    read_from_file(all_products, binance_products)
    for y in binance_products:
        binance_selectors.append(exchange + '.' + y['asset'] + '-' + y['currency'])

def check_if_crypto_pair_exists(crypto_pair):
    print('we are here')
    for x in binance_selectors:
        if x.endswith(crypto_pair) == True:
            print("Crypto pair found...")
            return
        else:
            print("crypto pair doesnt exist")
    #exit()
