from bs4 import BeautifulSoup
import glob, subprocess, json, re, shutil, os
import main
from utils import *


list_for_scraping = []
sim_results_dictionary = []
dict = {"currency_qnt": 1200,"hold_balance": 1000,"total_trades": 136,"total_sells": 70,"total_loses": 52,"strategy": "trend_ema","days": 14, "currency_exchange": "kraken.SAND-EUR", "win_loss": 0, "error_rate": 0, "asset": 0, "currency": 0, "exchange_id": 0, "start_date": 0, "end_date": 0, "period": "20200501 20200530"}
array_new = []
sim_output_file_name = ''
sim_results_file_name = ''

def create_scraping_list(crypto_pair):
    sim_files_list = glob.glob(os.getcwd() + "/simulations/" + crypto_pair + "/*")
    for one_file in sim_files_list:
    	if 'html' in one_file:
    		list_for_scraping.append(one_file.split('/')[-1])

def scrape(crypto_pair):
    global sim_results_dictionary
    create_scraping_list(crypto_pair)
    for html in list_for_scraping:
    	url = os.getcwd() + "/simulations/" + crypto_pair + "/" + html
    	page = open(url)
    	soup = BeautifulSoup(page.read(), 'html.parser')
    	raw_text = soup.code.get_text()
    	sim_results_dictionary = json.loads(raw_text[raw_text.find("{"):])
    	print(html.split("_")[-2:][0], html.split("_")[-2:][1].split('.')[0])
    	write_results_to_dictionary(html.split("_")[-2:][0] + "_" + html.split("_")[-2:][1].split('.')[0], crypto_pair)
    	move_scraped_files(html, crypto_pair)

def write_results_to_dictionary(period, crypto_pair):
    global dict, sim_results_dictionary, array_new
    dict["currency_qnt"] = sim_results_dictionary["simresults"]["currency"]
    dict["total_trades"] = sim_results_dictionary['simresults']['total_trades']
    dict["total_sells"] = sim_results_dictionary['simresults']['total_sells']
    dict["total_loses"] = sim_results_dictionary['simresults']['total_losses']
    dict["strategy"] = sim_results_dictionary['strategy']
    dict["currency_exchange"] = sim_results_dictionary['selector']['normalized']
    if sim_results_dictionary['simresults']['total_sells'] != 0:
    	dict["error_rate"] = sim_results_dictionary['simresults']['total_losses'] * 100 / (sim_results_dictionary['simresults']['total_sells'] + sim_results_dictionary['simresults']['total_losses'])
    if sim_results_dictionary['simresults']['total_sells'] != 0:
    	dict["win_loss"] = (sim_results_dictionary['simresults']['total_sells'] - sim_results_dictionary['simresults']['total_losses']) * 100 / sim_results_dictionary['simresults']['total_sells']
    	dict["currency"] = sim_results_dictionary['selector']['currency']
    	dict["asset"] = sim_results_dictionary['selector']['asset']
    	dict["exchange_id"] = sim_results_dictionary['selector']['exchange_id']
    	dict["start_date"] = sim_results_dictionary['start']
    	dict["hold_balance"] = sim_results_dictionary['simresults']['buy_hold']
    	dict["days"] = sim_results_dictionary['simresults']['length_days']
    	dict["period"] = period
    append_results_to_file(dict, crypto_pair)

def append_results_to_file(dictionary, crypto_pair):
    url = os.getcwd() + "/simulations/" + crypto_pair + "/"
    sim_output_file_name = url + "simulation_results" + "_" + str(dict["currency"]) + "_" + str(dict["asset"]) + "_" + get_today_date() + ".txt"
    with open(sim_output_file_name, 'a') as file:
        file.write('%s\n' % dictionary)
    file.close()

def move_scraped_files(file_name, crypto_pair):
    directory = os.getcwd() + r'/simulations/' + crypto_pair + '/'
    scraped_files_directory = os.getcwd() + r'/simulations/scraped/'
    shutil.move(directory + file_name, scraped_files_directory + file_name)
    print("File moved successfuly")

def get_sim_results_file_name():
    sim_results_file_name = "simulation_results" + "_" + dict["currency"] + "_" + dict["asset"] + "_" + get_today_date() + ".txt"
    return sim_results_file_name
