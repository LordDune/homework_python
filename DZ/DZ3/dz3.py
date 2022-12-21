import random

def rand_int(value):
    k = []
    for i in range(0,value):
        k.append(random.randint(0,20))
    return k

def check_exit(text):
    if(text.lower() == 'q'):
            print("\n" * 20)
            return 1

print ("Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]")
while True:
    try:
        text = (input(("Введите число элементов массива или наберите 'q' для выхода: ")))
        if check_exit(text) == 1:
            break
        list_1 = rand_int(int(text))
        print(list_1)
        x = int(input("Введите искомое число: "))
        count = 0
        for i in list_1:
            if x == i:
                count += 1
        print(f"Число {x} встречается {count} раз")

    except:
        print("Некорректный ввод")
        continue

print ("Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.")
while True:
    try:
        text = (input(("Введите число элементов массива или наберите 'q' для выхода: ")))
        if check_exit(text) == 1:
            break
        s = rand_int(int(text))
        print(s)
        n = int(input("Введите искомое число: "))
        n_near = s[0]
        delta = abs(n - n_near)

        for i in s:
            x = abs(n - i)
            if (x < delta):
                delta = x
                n_near = i
            elif (x == delta):
                if i < n_near:
                    n_near = i 

        print(f"Ближайшее число: {n_near}")
                
    except:
        print("Некорректный ввод")
        continue

print ("Задача 20: Напишите программу, которая вычисляет стоимость введенного пользователем слова.")
while True:
    try:
        text = input("Введите слово или наберите 'q' для выхода: ").upper()
        if check_exit(text) == 1:
            break
        
        dictionary = \
        {
            'A': '1', 'L': '1', 'W': '4',   'А': '1', 'К': '2', 'Х': '5',
            'B': '3', 'M': '3', 'X': '8',   'Б': '3', 'Л': '2', 'Ц': '5',
            'C': '3', 'N': '1', 'Y': '4',   'В': '1', 'М': '2', 'Ч': '5',
            'D': '2', 'O': '1', 'Z': '10',  'Г': '3', 'Н': '1', 'Ш': '8',
            'E': '1', 'P': '3',             'Д': '2', 'О': '1', 'Щ': '10',
            'F': '4', 'Q': '10',            'Е': '1', 'П': '2', 'Ъ': '10',
            'G': '2', 'R': '1',             'Ё': '3', 'Р': '1', 'Ы': '4',
            'H': '4', 'S': '1',             'Ж': '5', 'С': '1', 'Ь': '3',
            'I': '1', 'T': '1',             'З': '5', 'Т': '1', 'Э': '8',
            'J': '8', 'U': '1',             'И': '1', 'У': '2', 'Ю': '8',
            'K': '5', 'V': '4',             'Й': '4', 'Ф': '10', 'Я': '3',       
        }

        value = 0
        for i in text:
            if i in dictionary:
                value += int(dictionary[i])
        print(value)

    except:
        print("Некорректный ввод")
        continue