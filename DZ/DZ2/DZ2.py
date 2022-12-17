import random
print ("Задача 10 \n\
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. \n\
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. \n\
Выведите минимальное количество монет, которые нужно перевернуть.")
while True:
    try:
        text = input("Введите количество монет или наберите 'q' для выхода: ")
        if(text.lower() == 'q'):
            print("\n" * 20)
            break
        n = int(text)
        if (n < 0):
            print("Введите целое положительное число")
            print("\n" * 20)
            continue
        m = []
        sum = 0
        for i in range(n):
            i = random.randint(0,1)
            m.append(i)
            sum += i
        print(m)
        if (sum < n-sum):
            count = sum
        else:
            count = n-sum
        if (count%10 > 4 or count%10 == 0 or 10 < count < 15):
            case = '' 
        elif (5 > count%10 > 1):
            case = 'ы'
        else:
            case = 'у'
        print(f"Нужно перевернуть {count} монет{case}")
    except:
        print("Некорректный ввод")
        continue

print ("Задача 12 \n\
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. \n\
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. \n\
Он называет сумму этих чисел S и их произведение P.\n\
Помогите Кате отгадать задуманные Петей числа.")
while True:
    try:
        s_str = input("Введите сумму двух чисел или наберите 'q' для выхода: ")
        if(s_str.lower() == 'q'):
            print("\n" * 20)
            break
        s = int(s_str)
        p = (int(input("Введите произведение двух чисел: ")))
        if (s < 0 or p < 0):
            print("Некорректный ввод. Числа должны быть натуральным (целыми и положительными)")
            print("\n" * 20)
            continue
        d = s ** 2 - 4*p
        if (d < 0):
            print("Решений нет")
            continue
        x = (s + d ** 0.5) / 2 
        y = (s - d ** 0.5) / 2
        if (x%1 == 0 and y%1 ==0):
            print(f"Загаданные числа: {round(x)} и {round(y)}")
        else:
            print("Целочисленных решений нет")
    except:
        print("Некорректный ввод")
        continue

print ("Задача 14 \n\
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.")
while True:
    try:
        n = input("Введите положительное число или наберите 'q' для выхода: ")
        if(n.lower() == 'q'):
            print("\n" * 20)
            break
        s = int(n)
        if (s < 1):
            continue
        k = 1
        count = 0
        while(k <= s):
            print(k)
            count += 1
            k = 2**count
    except:
        print("Некорректный ввод")
        continue