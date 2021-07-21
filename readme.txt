Hello! Welcome to Zenbot trading bot script. You can download Zenbot here: https://github.com/DeviaVir/zenbot
After installing Zenbot, put these script files into main directory of Zenbot.

 With this script you will get data how 40 different strategies were profitable or made losses during period of your choice. 
 All this data will be shown in HTML table so you will see how different strategies were performing during year, half year or other period.
 Based on this historical data you will be able to see larger picture how different strategies work and decide which strategy to use for trading.
 All you need is to provide cryptocurrency pair and period you are interested in.

 Steps which are performed by script are:
 1) Generates backfilling commands for Zenbot and run them as a subprocess for downloading real historical
 data from Binance.eu exchange for provided period, and cryptocurrency-pair.
 2) Generates and run Zenbot simulation commands on provided period and cryptocurrency pair which generates HTML file for each strategy.
 3) Scrapes all HTML files of simulations into .txt file.
 4) Shows all data in a HTML page table.
 
 Be patient. Steps 1 and 2 takes some time. But don't worry all process will be shown on a screen while you are doing anything else.
