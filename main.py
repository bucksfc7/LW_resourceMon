
from datetime import datetime
from os.path import dirname
import os.path
import csv
import time
import pip
import subprocess
import sys
import json
import psutil


#installs psutil
#def install_and_import(package):
#    import importlib
#    try:
#        importlib.import_module(package)
#    except ImportError:
#        import pip
#        pip.main(['install', package])
#    finally:
#        globals()[package] = importlib.import_module(package)
#install_and_import('psutil')

#variables

user_time = 1
# my attempt at a universal path
expand = (dirname(__file__))
folder = os.path.join(expand, 'monitor.csv')

#gets user input
#user_time = input('\n\nHow many minutes would you like to monitor?\nPlease input minutes and press enter: ')


config_file = open('config.json',)
data = json.load(config_file)
print('View settings:\n')
print(data)
utime = data['utime']
delay_interval = data['delay_interval']
max_pct = data['max_pct']
#changes user input from string to float
#user_float = float(user_time)

#sets the sketch to run for time 60 sec x 15; we can replace with chron
t_end = time.time() + 60 * utime
#gets delay inerval

#delay_interval = float(input('Input how fast you want the CPU/Memory to be polled and press enter. \n Seconds: '))
print('Results will be recorded to file located in ' + expand)
print('\n\nYYYY_MM_DD_HH:MM:SS CPU% RAM%')




#main program
while time.time() < t_end:
    def main():
        # date time stamp
        dt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        # load average for 1 minute
        #cpu_load = psutil.getloadavg()
        # grabs the CPU percent from psutil
        cpu_percent = [psutil.cpu_percent()]
        #change cpu_percent from list to int However it definatley is not working
        cpu_int = map(int,cpu_percent)
        # grabs the RAM usage from psutil
        mem_usage = [psutil.virtual_memory().percent]
        # setup parameter output
        params = [dt]
        params.extend(cpu_percent)
        params.extend(mem_usage)
        time.sleep(delay_interval)

        # sets up the line for input into the CSV
        line = ' '.join([str(x) for x in params])
        # starts the CSV writing
        with open(folder, 'a') as f:
            f.write(line + '\n')
        # gives some user feedback for debugging
        print(line)

        #if cpu_int > max_pct :
            #print('finally!!!!!!!!!!!!!')
            #time.sleep(3)

    if __name__ == "__main__":
        main()