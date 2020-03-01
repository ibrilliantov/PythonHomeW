import csv


users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open("exportusers.csv", "w", encoding="utf-8") as f:
    fields = ['name', 'age', 'job']
    writen = csv.DictWriter(f, fields, delimiter=',')
    writen.writeheader()
    for name in users:
        writen.writerow(name)