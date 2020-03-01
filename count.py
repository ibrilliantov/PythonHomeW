from collections import Counter

phones = ["iphone", "samsung", "xiaomi", "LG", "iphone", "iphone", "LG"]

count = Counter(phones)
print(count)

text = "Ехал Грека через рекуБ видит Грека в реке рак.".lower().replace(" ", "")
count = Counter(text)
print(count)