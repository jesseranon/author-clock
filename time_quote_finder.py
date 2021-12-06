from csv import DictReader
from datetime import datetime
import random

def find_time_quote(): 
    with open('time-quotes-litclock-combined.csv', 'r') as read_obj:

        # now = datetime.now()
        now_time = '0:00' #f"now.hours():now.minutes()"
        filtered_results = []

        csv_dict_reader = DictReader(read_obj)
        column_names = csv_dict_reader.fieldnames
        # print(column_names)
        for row in csv_dict_reader:
            # print(row['time-of-quote'], row['author'])
            if row['time-of-text'] == now_time: #change to result of current time conversion function
                filtered_results.append(row)

        if len(filtered_results) > 0:
            return filtered_results[random.randint(0,len(filtered_results)-1)]
        else:
            return f"No quotes found for {now_time}"