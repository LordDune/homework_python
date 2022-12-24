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

print ("Задача 22: Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.")
while True:
    try:
        text = (input(("Введите число элементов первого списка или наберите 'q' для выхода: ")))
        if check_exit(text) == 1:
            break
        n = rand_int(int(text))
        print(n)
        m = rand_int(int(input("Введите количество элементов второго списка: ")))
        print(m)

        a = list(set(n).intersection(set(m)))
        a.sort()
        print(f"Результат: {a}")

    except:
        print("Некорректный ввод")
        continue

print ("Задача 24: Нахождение максимального числа ягод, которое может собрать за один заход собирающий модуль")
while True:
    try:
        text = (input("Введите количество кустов на грядке: или наберите 'q' для выхода: "))
        if check_exit(text) == 1:
            break
        n = rand_int(int(text))
        print(n)
        n.insert(0,n[-1]) # добавляем в начало списка последний элемент, чтобы можно было проверить первый элемент
        n.append(n[1]) # добавляем в конец списка первый элемент, чтобы можно было проверить последний элемент
        max = 0
        index = 0
        for i in range(1,len(n)-1):
            sum = n[i] + n[i-1] + n[i+1]
            if sum > max:
                max = sum
                index = i
        print(f"Максимальное число - {max} ягод можно собрать с {index} куста и двух соседних (нумерация начинается с 1)")

    except:
        print("Некорректный ввод")
        continue