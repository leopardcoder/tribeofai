import glob, subprocess, json, re, shutil
import main
from preparation_data import *
from utils import *


months_list = ['20200601 20200630', '20200701 20200731', '20200801 20200831',
'20200901 20200930', '20201001 20201031', '20201101 20201130',
'20201201 20201230', '20210101 20210131', '20210201 20200228',
'20210301 20200331', '20210401 20200430', '20210501 20200531',
'20210601 20210630']
binance_sim_commands_list = []
get_binance_sim_commands_list = []
binance_sim_commands_final_list = []
# to many prints, have a silent option in configuration... a) only errors b) ... c) ...

def get_binance_sim_commands_list(start_date, end_date, exchange, crypto_pair,
strategies):
    command = "./zenbot.sh sim " + exchange + "." + crypto_pair
    for x in strategies:
        binance_sim_commands_list.append(command + " --strategy " + x + " " + \  # code formaters google to do everything for me.
        "--filename " + os.getcwd() + "/simulations/" + crypto_pair + \ # f-string google ..
        "/" + x + "_")  # /simulations/ used to often, use configuration. create json file with folder location

    for i in range(start_date, end_date+1):
        for z in binance_sim_commands_list:
            binance_sim_commands_final_list.append(z + exchange + "_" + \ # f-string google .. will look beautiful
            crypto_pair + "_" + months_list[i].split(" ")[0] + \ # create extra variables for readability...
            "_" + months_list[i].split(" ")[1] + ".html" + \
            " --start " + months_list[i].split(' ')[0] + \
            " --end " + months_list[i].split(' ')[1] + \
            " --buy_pct 1 " + "--sell_pct 1 " + "--silent")

    print(binance_sim_commands_final_list)

def zenbot_simulate_now(sim_commands_list):
    for x in sim_commands_list:
        print("Simulation started... It will take some time if crypto-pair"
        + "has many trades.")
        subprocess.run(x, shell=True)
