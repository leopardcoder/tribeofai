from bs4 import BeautifulSoup
import glob, subprocess, json, re, shutil, os
import main
from utils import *

list_for_scraping = []
sim_results = []
crypto_info = {"currency_qnt": 1200,"hold_balance": 1000,"total_trades": 136,
"total_sells": 70,"total_loses": 52,"strategy": "trend_ema","days": 14,
"currency_exchange": "kraken.SAND-EUR", "win_loss": 0, "error_rate": 0,
"asset": 0, "currency": 0, "exchange_id": 0, "start_date": 0, "end_date": 0,
"period": "20200501 20200530"}
sim_output_file_name = ''
sim_results_file_name = ''

def create_scraping_list(crypto_pair):
    sim_files_list = glob.glob(os.getcwd() + "/simulations/" + crypto_pair + "/*")
    for one_file in sim_files_list:
    	if 'html' in one_file:
    		list_for_scraping.append(one_file.split('/')[-1])

def scrape(crypto_pair):
    global sim_results
    create_scraping_list(crypto_pair)
    for html in list_for_scraping:
    	url = os.getcwd() + "/simulations/" + crypto_pair + "/" + html
    	page = open(url)
    	soup = BeautifulSoup(page.read(), 'html.parser')
    	raw_text = soup.code.get_text()
    	sim_results = json.loads(raw_text[raw_text.find("{"):])
    	print(html.split("_")[-2:][0], html.split("_")[-2:][1].split('.')[0])
    	write_results_to_dictionary(html.split("_")[-2:][0] + "_" \
        + html.split("_")[-2:][1].split('.')[0], crypto_pair)
    	move_scraped_files(html, crypto_pair)

def write_results_to_dictionary(period, crypto_pair):
    global crypto_info, sim_results
    crypto_info["currency_qnt"] = sim_results["simresults"]["currency"]
    crypto_info["total_trades"] = sim_results['simresults']['total_trades']
    crypto_info["total_sells"] = sim_results['simresults']['total_sells']
    crypto_info["total_loses"] = sim_results['simresults']['total_losses']
    crypto_info["strategy"] = sim_results['strategy']
    crypto_info["currency_exchange"] = sim_results['selector']['normalized']
    if sim_results['simresults']['total_sells'] != 0:
    	crypto_info["error_rate"] = sim_results['simresults']['total_losses'] \
        * 100 / (sim_results['simresults']['total_sells'] + \
        sim_results['simresults']['total_losses'])
    if sim_results['simresults']['total_sells'] != 0:
    	crypto_info["win_loss"] = (sim_results['simresults']['total_sells'] \
        - sim_results['simresults']['total_losses']) * 100 / \
        sim_results['simresults']['total_sells']
    	crypto_info["currency"] = sim_results['selector']['currency']
    	crypto_info["asset"] = sim_results['selector']['asset']
    	crypto_info["exchange_id"] = sim_results['selector']['exchange_id']
    	crypto_info["start_date"] = sim_results['start']
    	crypto_info["hold_balance"] = sim_results['simresults']['buy_hold']
    	crypto_info["days"] = sim_results['simresults']['length_days']
    	crypto_info["period"] = period
    append_results_to_file(crypto_info, crypto_pair)

def append_results_to_file(dictionary, crypto_pair):
    url = os.getcwd() + "/simulations/" + crypto_pair + "/"
    sim_output_file_name = url + "simulation_results" + "_" + \
    str(crypto_info["currency"]) + "_" + str(crypto_info["asset"]) + "_" + \
    get_today_date() + ".txt"
    with open(sim_output_file_name, 'a') as file:
        file.write('%s\n' % dictionary)
    file.close()

def move_scraped_files(file_name, crypto_pair):
    directory = os.getcwd() + r'/simulations/' + crypto_pair + '/'
    scraped_files_directory = os.getcwd() + r'/simulations/scraped/'
    shutil.move(directory + file_name, scraped_files_directory + file_name)
    print("File moved successfuly")

def get_sim_results_file_name():
    sim_results_file_name = "simulation_results" + "_" + crypto_info["currency"] + \
    "_" + crypto_info["asset"] + "_" + get_today_date() + ".txt"
    return sim_results_file_name
