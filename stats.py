import json
from datetime import datetime


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
            date = datetime.strptime(answer['date'], '%Y-%m-%d %H:%M')
            date_str = f'{date.year}-{date.month}-{date.day} {date.hour}'
            if date_str not in date_map_answers:
                date_map_answers[date_str] = 1
            else:
                date_map_answers[date_str] += 1
        return list(date_map_answers.items())

    def save_exam(self, exam):
        with open(self.file_path, 'w', encoding='utf-8') as fh:
            exam_result = exam.generate_result()
            self.data['exams'].append(exam_result)
            json.dump(self.data, fh, indent=4, ensure_ascii=False)

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

    def get_exams(self):
        return self.data['exams']
