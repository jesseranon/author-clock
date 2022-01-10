import sys
import os
import random
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
from csv import DictReader

def find_time_quote(s): 
    with open(f'{libdir}/time-quotes-litclock-combined.csv', 'r') as read_obj:

        now_time = s
        filtered_results = []

        csv_dict_reader = DictReader(read_obj)
        
        # print(column_names)
        for row in csv_dict_reader:
            # print(row['time-of-quote'], row['author'])
            if row['time-of-text'] == now_time: #change to result of current time conversion function
                filtered_results.append(row)

        if len(filtered_results) > 0:
            return random.choice(filtered_results)
        else:
            return False