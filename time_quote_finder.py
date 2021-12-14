from csv import DictReader
from time_quote_generator import generate_time_quote
import random

def find_time_quote(s): 
    with open('time-quotes-litclock-combined.csv', 'r') as read_obj:

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
            return generate_time_quote(s)