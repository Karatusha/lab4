import csv
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('uk_UA')

po_batkovi = {
    'male': ['Олександрович', 'Іванович', 'Петрович', 'Миколайович', 'Васильович', 'Сергійович', 'Андрійович',
             'Вікторович', 'Юрійович', 'Романович', 'Максимович', 'Дмитрович', 'Артемович', 'Ігорович', 'Володимирович',
             'Олексійович', 'Євгенович', 'Денисович', 'Владиславович', 'Павлович'],
    'female': ['Олександрівна', 'Іванівна', 'Петрівна', 'Миколаївна', 'Василівна', 'Сергіївна', 'Андріївна',
               'Вікторівна', 'Юріївна', 'Романівна', 'Максимівна', 'Дмитрівна', 'Артемівна', 'Ігорівна',
               'Володимирівна', 'Олексіївна', 'Євгенівна', 'Денисівна', 'Владиславівна', 'Павлівна']
}

with open('employees.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Прізвище', 'Ім\'я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто',
                  'Адреса проживання', 'Телефон', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(2000):
        gender = 'female' if random.random() < 0.4 else 'male'
        if gender == 'female':
            first_name = fake.first_name_female()
            po_batkovi_name = random.choice(po_batkovi['female'])
        else:
            first_name = fake.first_name_male()
            po_batkovi_name = random.choice(po_batkovi['male'])

        birth_date = fake.date_between_dates(date_start=datetime(1938, 1, 1), date_end=datetime(2008, 1, 1))

        employee = {
            'Прізвище': fake.last_name_nonbinary() if gender not in ("male", "female") else fake.last_name(),
            'Ім\'я': first_name,
            'По батькові': po_batkovi_name,
            'Стать': gender,
            'Дата народження': birth_date.strftime('%Y-%m-%d'),
            'Посада': fake.job(),
            'Місто': fake.city(),
            'Адреса проживання': fake.address(),
            'Телефон': fake.phone_number(),
            'Email': fake.email()
        }
        writer.writerow(employee)