
with open("referat.txt", "r", encoding="utf-8") as f:
    content = f.read()
    r = len(content)
    a = "длина строки:" + " " + str(r)
    print(a)

    wat = len(content.split())
    b = "кол-во слов:" + " " + str(wat)
    print(b)

    newtext = content.replace(".", "!")
    print(newtext)

    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(a + '\n')
    with open('referat2.txt', 'a', encoding='utf-8') as f2:
        f2.write(b + '\n')
    with open('referat2.txt', 'a', encoding='utf-8') as f2:
        f2.write(newtext)
