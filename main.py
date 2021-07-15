from preparation_data import *
from utils import *
from back_filling import *
from simulation import *
from scraping import *

crypto_pair = ''

if __name__ == "__main__":

    print( "\n" +
    " Hello! Welcome to most profitable trading strategies searcher."
    + "\n"
        + "\n Here you will get data about 40 different strategies profits or losses."
        + "\n Based on this data you will be able to decide which strategy to choose."
        + "\n All you need is to provide cryptocurrency pair and period you are "
        + "\n interested in."
        + "\n"
        + "\n Steps which are performed by program are:"
        + "\n 1) download real historical data from Binance.eu exchange for provided period."
        + "\n 2) run simulation on provided period and cryptocurrency pair, generate HTML for each strategy."
        + "\n 3) scrape all HTML files of simula tions into .txt file."
        + "\n 4) show all data in a html page."
        + "\n"
        + "\n Be patient. Steps 1 and 2 takes some time. But don't worry all process"
        + "\n will be shown on a screen while you are doing anything else."
        + "\n ")
    start_case = input(" Do you want to scrape simulation files and see them in a table and skip first two steps? y/n ")


    def start_at_step(answer):
        if start_case == 'y':
            # zenbot_simulate_now(binance_sim_commands_list2)
            crypto_pair_test = input("Enter crypto pair: ex. ETH-BTC ")
            scrape(crypto_pair_test)
        elif start_case == 'n':
            global crypto_pair
            crypto_pair = input("Enter crypto pair: ex. ETH-BTC ")
            get_binance_selector()
            check_if_crypto_pair_exists(crypto_pair)
            create_dir(crypto_pair)
            period = input("Enter period you are interested in: YYYYMMDD-YYYYMMDD ")
            #get_period_months(period)
            generate_backfill_commands_provided(period, crypto_pair)
            get_strategy_names()
            get_binance_sim_commands_list(generate_backfill_commands_provided.start_date, generate_backfill_commands_provided.end_date, 'binance', crypto_pair, strategies)
            zenbot_simulate_now(binance_sim_commands_final_list)

            scrape(crypto_pair)
        else:
            print ('unknown command')
            return

    start_at_step(start_case)
