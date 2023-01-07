import json
from datetime import datetime

data = {}
with open('tests/demo_stats.json', encoding='utf-8') as fh:
    data = json.load(fh)
    answers_correct = data['answers']['correct']
    answers_wrong = data['answers']['wrong']
    exams = data['exams']

    for answer in answers_correct:
        date_str = answer['date']
        date_big, date_small = date_str.split(' ')
        year, month, day = date_big.split('-')
        hour, minute = date_small.split(':')
        correct_str = f"{year}-{f'0{month}' if len(month) == 1 else month}-{f'0{day}' if len(day) == 1 else day} {f'0{hour}' if len(hour) == 1 else hour}:{f'0{minute}' if len(minute) == 1 else minute}"
        # print(correct_str)
        dt = datetime.fromisoformat(correct_str)
        new_date = dt.strftime('%d-%m-%Y %H:%M')
        new_date_str = str(new_date)

        answer['date'] = new_date_str

    for answer in answers_wrong:
        date_str = answer['date']
        date_big, date_small = date_str.split(' ')
        year, month, day = date_big.split('-')
        hour, minute = date_small.split(':')
        correct_str = f"{year}-{f'0{month}' if len(month) == 1 else month}-{f'0{day}' if len(day) == 1 else day} {f'0{hour}' if len(hour) == 1 else hour}:{f'0{minute}' if len(minute) == 1 else minute}"
        # print(correct_str)
        dt = datetime.fromisoformat(correct_str)
        new_date = dt.strftime('%d-%m-%Y %H:%M')
        new_date_str = str(new_date)

        answer['date'] = new_date_str

    for exam in exams:
        date_str = exam['date']
        date_big, date_small = date_str.split(' ')
        year, month, day = date_big.split('-')
        hour, minute = date_small.split(':')
        correct_str = f"{year}-{f'0{month}' if len(month) == 1 else month}-{f'0{day}' if len(day) == 1 else day} {f'0{hour}' if len(hour) == 1 else hour}:{f'0{minute}' if len(minute) == 1 else minute}"
        # print(correct_str)
        dt = datetime.fromisoformat(correct_str)
        new_date = dt.strftime('%d-%m-%Y %H:%M')
        new_date_str = str(new_date)

        exam['date'] = new_date_str

with open('tests/demo_stats.json', 'w', encoding='utf-8') as fh:
    json.dump(data, fh, indent=4, ensure_ascii=False)
