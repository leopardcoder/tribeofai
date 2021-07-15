import glob, subprocess, json, re, shutil
import main
from preparation_data import *
from utils import *


months_list = ['20200601 20200630', '20200701 20200731', '20200801 20200831', '20200901 20200930', '20201001 20201031', '20201101 20201130', '20201201 20201230', '20210101 20210131', '20210201 20200228', '20210301 20200331', '20210401 20200430', '20210501 20200531', '20210601 20210630']
binance_sim_commands_list = []
get_binance_sim_commands_list = []
binance_sim_commands_final_list = []


def get_binance_sim_commands_list(start_date, end_date, exchange, crypto_pair, strategies):
    command = "./zenbot.sh sim " + exchange + "." + crypto_pair
    for x in strategies:
        binance_sim_commands_list.append(command + " --strategy " + x + " " + "--filename " + "/home/linas/zenbot/simulations/" + crypto_pair + "/" + x + "_")
    for i in range(start_date, end_date+1):
        for z in binance_sim_commands_list:
            binance_sim_commands_final_list.append(z + exchange + "_" + crypto_pair + "_" + months_list[i].split(" ")[0] + "_" + months_list[i].split(" ")[1] + ".html" + " --start " + months_list[i].split(' ')[0] + " --end " + months_list[i].split(' ')[1] + " --buy_pct 1 " + "--sell_pct 1 " + "--silent")
    print(binance_sim_commands_final_list)

def zenbot_simulate_now(sim_commands_list):
    for x in sim_commands_list:
            # array = x.split(" ")
    		# subprocess_array = array[0:1] + [array[1] + " " + array[2]] + [array[3] + " " + array[4]] + [array[5] + " " + array[6]] + [array[7] + " " + array[8]] + [array[9] + " " + array[10]]
    		# backfill_process = subprocess.Popen(subprocess_array,  stdout=subprocess.PIPE)
            print("Simulation started... It will take some time if crypto-pair has many trades.")
            subprocess.run(x, shell=True)
