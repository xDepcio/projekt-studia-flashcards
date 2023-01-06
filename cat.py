import json
from datetime import datetime, timedelta
from time import time


with open('stats.json') as fh:
    data = json.load(fh)
    correct = data['answers']['correct']
    wrong = data['answers']['wrong']
    current_dt = datetime.fromtimestamp(time())
    categories = [str(current_dt.strftime('%d-%m-%Y'))]
    display_range = 30 - 1
    for i in range(display_range):
        dt = current_dt - timedelta(days=i+1)
        categories.insert(0, str(dt.strftime('%d-%m-%Y')))
    print(categories)
    print(len(categories))
