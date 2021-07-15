import subprocess
import main
from utils import *

user_entered_period = []
months_list = ['20200601 20200630', '20200701 20200731', '20200801 20200831', '20200901 20200930', '20201001 20201031', '20201101 20201130', '20201201 20201230', '20210101 20210131', '20210201 20200228', '20210301 20200331', '20210401 20200430', '20210501 20200531', '20210601 20210630']

def generate_backfill_commands_provided(period, crypto_pair):
    # for day in period_days_array:
    #    command = './zenbot.sh backfill binance.' + crypto_pair + ' --start ' + day + ' --end ' + day
    #    zenbot_backfill_now(command)

    generate_backfill_commands_provided.start_date = list(map(lambda x: x[0:6], months_list)).index(period.split('-')[0][0:6])
    generate_backfill_commands_provided.end_date = list(map(lambda x: x[0:6], months_list)).index(period.split('-')[1][0:6])



    for i in range(generate_backfill_commands_provided.start_date, generate_backfill_commands_provided.end_date+1):
        user_entered_period.append(i)
        command = './zenbot.sh backfill binance.' + crypto_pair + ' --start ' + months_list[i].split(' ')[0] + ' --end ' + months_list[i].split(' ')[1]
        zenbot_backfill_now(command)

def backfill_until_today(crypto_pair):
    command = './zenbot.sh backfill binance.' + crypto_pair +  ' --end ' + get_today_date_zenbot_format()
    zenbot_backfill_now(command)

def zenbot_backfill_now(command):
    subprocess.run(command, shell=True)
