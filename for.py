# for number in range(3):
#     print(f'Hello world {number}')


# example_string = "i learn python language"
#
# for word in example_string.split():
#     print(f'Длинна слова "{word}": {len(word)}')

#
students_scores = [1, 21, 19, 6, 5]

# print(f'средняя оценка {sum(students_scores) / len(students_scores)}')

scores_sum = 0
for score in students_scores:
    scores_sum += score
    print(scores_sum)

print(f'средняя оценка {scores_sum/ len(students_scores)}')
# from lessonIf import discounted
#
# stock = [
# 		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
# 		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
# 		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
# ]
#
# for phone in stock:
#     print(phone)
#     phone["final_price"] = discounted(phone["price"], phone["discount"], name=phone["name"])
#     print(phone)
#     print("----")

