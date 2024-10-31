import csv
from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import pandas as pd

try:
    with open('employees.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        gender_counts = {'male': 0, 'female': 0}
        age_groups = {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}
        gender_age_groups = {
            'male': {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0},
            'female': {'younger_18': 0, '18-45': 0, '45-70': 0, 'older_70': 0}
        }

        for row in reader:
            gender_counts[row['Стать']] += 1

            birth_date_str = row['Дата народження']
            birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            age = (date.today() - birth_date) // timedelta(days=365.2425)

            if age < 18:
                age_groups['younger_18'] += 1
                gender_age_groups[row['Стать']]['younger_18'] += 1
            elif 18 <= age <= 45:
                age_groups['18-45'] += 1
                gender_age_groups[row['Стать']]['18-45'] += 1

            elif 45 < age <= 70:
                age_groups['45-70'] += 1
                gender_age_groups[row['Стать']]['45-70'] += 1

            else:
                age_groups['older_70'] += 1
                gender_age_groups[row['Стать']]['older_70'] += 1
        print("Ok")

        print("Кількість співробітників за статтю:", gender_counts)
        plt.figure(figsize=(6, 4))
        plt.bar(gender_counts.keys(), gender_counts.values())
        plt.title('Розподіл співробітників за статтю')
        plt.xlabel('Стать')
        plt.ylabel('Кількість')

        print("Кількість співробітників за віковими групами:", age_groups)
        plt.figure(figsize=(8, 5))
        plt.bar(age_groups.keys(), age_groups.values())
        plt.title('Розподіл співробітників за віковими групами')
        plt.xlabel('Вікова група')
        plt.ylabel('Кількість')

        for gender in gender_age_groups:
            print(f"Кількість співробітників {gender} статі за віковими групами:", gender_age_groups[gender])
            plt.figure(figsize=(8, 5))
            plt.bar(gender_age_groups[gender].keys(), gender_age_groups[gender].values())
            plt.title(f'Розподіл співробітників {gender} статі за віковими групами')
            plt.xlabel('Вікова група')
            plt.ylabel('Кількість')

        plt.show()


except FileNotFoundError:
    print("Повідомлення про відсутність або проблеми при відкритті файлу CSV.")


except Exception as e:
    print(f"Помилка: {e}")