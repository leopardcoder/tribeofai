from preparation_data import *
from utils import *
from back_filling import *
from simulation import *
from scraping import *

crypto_pair = ''

def start_at_step(answer):
    if start_case == 'y':
        crypto_pair_test = input("Enter crypto pair: ex. ETH-BTC ")
        scrape(crypto_pair_test)
    elif start_case == 'n':
        crypto_pair = input("Enter crypto pair: ex. ETH-BTC ")
        get_binance_selector()
        check_if_crypto_pair_exists(crypto_pair)
        create_dir(crypto_pair)
        period = input("Enter period you are interested in: YYYYMMDD-YYYYMMDD ")
        generate_backfill_commands(period, crypto_pair)
        get_strategy_names()
        get_binance_sim_commands_list(generate_backfill_commands.start_date,
        generate_backfill_commands.end_date, 'binance', crypto_pair,
        strategies)
        zenbot_simulate_now(binance_sim_commands_final_list)
        scrape(crypto_pair)
    else:
        print ('Unknown command')
        return

if __name__ == "__main__":

    read_info_file('readme.txt')
    start_case = input(" Do you want to scrape simulation files and see " +
    " them in a table and skip first two steps? y/n ")

    start_at_step(start_case)
