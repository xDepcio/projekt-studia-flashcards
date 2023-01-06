import json
from datetime import datetime, timedelta
import math
from time import time


class Stats:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        with open(self.file_path, encoding='utf-8') as fh:
            stats = json.load(fh)
            self.data = stats

    def reload_stats(self):
        with open(self.file_path, encoding='utf-8') as fh:
            stats = json.load(fh)
            self.data = stats

    # def save_stats(self):
    #     with open(self.file_path, 'w', encoding='utf-8') as fh:
    #         json.dump(self.data, fh, indent=4, ensure_ascii=False)

    def get_date_answers_count(self, answer_type):
        date_map_answers = {}
        for answer in self.data['answers'][answer_type]:
            date = datetime.strptime(answer['date'], '%d-%m-%Y %H:%M')
            date_str = f'{date.year}-{date.month}-{date.day}'
            if date_str not in date_map_answers:
                date_map_answers[date_str] = 1
            else:
                date_map_answers[date_str] += 1
        return list(date_map_answers.items())

    def get_answers_date_range_count(self, days_range, from_date):
        timestamp = from_date.timestamp()
        days = self._get_days_list(timestamp, days_range, '%d-%m-%Y')
        days_dict = {}
        for day in days:
            days_dict[day] = {
                'correct': 0,
                'wrong': 0,
            }

        answers_c = self.data['answers']['correct']
        for answer in answers_c:
            answ_date = answer['date'].split(' ')[0]
            if answ_date in days_dict:
                days_dict[answ_date]['correct'] += 1

        answers_w = self.data['answers']['wrong']
        for answer in answers_w:
            answ_date = answer['date'].split(' ')[0]
            if answ_date in days_dict:
                days_dict[answ_date]['wrong'] += 1

        correct = []
        wrong = []
        for day in days_dict.values():
            correct.append(day['correct'])
            wrong.append(day['wrong'])

        return correct, wrong, days

    def _get_days_list(self, timestamp, days_range, format):
        timestamp_day = datetime.fromtimestamp(timestamp)
        timestamp_day_str = str(timestamp_day.strftime(format))
        days_list = [timestamp_day_str]
        for i in range(days_range - 1):
            dt = timestamp_day - timedelta(days=i+1)
            dt_str = str(dt.strftime(format))
            days_list.insert(0, dt_str)
        return days_list

    def save_exam(self, exam):
        with open(self.file_path, 'w', encoding='utf-8') as fh:
            exam_result = exam.generate_result()
            self.data['exams'].append(exam_result)
            self.data['answersToLastExam'] = self.answers_count()
            json.dump(self.data, fh, indent=4, ensure_ascii=False)
        self.reload_stats()

    def answers_since_last_exam(self):
        return self.answers_count() - self.data['answersToLastExam']

    def save_use_time(self, current_session_time):
        with open(self.file_path, 'w', encoding='utf-8') as fh:
            self.data['appUseTimeSeconds'] += current_session_time
            json.dump(self.data, fh, indent=4, ensure_ascii=False)
        self.reload_stats()

    def app_use_time(self):
        time_s = self.data['appUseTimeSeconds']
        days = math.floor(time_s / 86400)
        hours = math.floor((time_s % 86400) / 3600)
        minutes = math.floor((time_s % 3600) / 60)
        return days, hours, minutes

    def answers_count(self):
        correct_len = len(self.data['answers']['correct'])
        wrong_len = len(self.data['answers']['wrong'])
        return correct_len + wrong_len

    def correct_answers_count(self):
        return len(self.data['answers']['correct'])

    def wrong_answers_count(self):
        return len(self.data['answers']['wrong'])

    def answers_accuracy(self):
        correct = self.correct_answers_count()
        wrong = self.wrong_answers_count()
        ratio = round(correct/(correct+wrong)*100, 2)
        return ratio

    def exams_count(self):
        return len(self.get_exams())

    def exams_avg_accuracy(self):
        total = sum([exam['percentage'] for exam in self.get_exams()])
        avg = round(total/len(self.get_exams()), 2)
        return avg

    def save_answer(self, answer):
        with open(self.file_path, 'w', encoding='utf-8') as fh:
            answer_str = {
                "originLang": answer.expected,
                "learningLang": answer.to_be_guessed,
                "date": answer.date
            }
            if answer.is_correct:
                self.data['answers']['correct'].append(answer_str)
            else:
                self.data['answers']['wrong'].append(answer_str)
            json.dump(self.data, fh, indent=4, ensure_ascii=False)
        self.reload_stats()

    def get_exams(self):
        return self.data['exams']
