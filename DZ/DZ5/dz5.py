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

print ("Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.")
while True:
    try:
        text = (input(("Введите число или наберите 'q' для выхода: ")))
        if check_exit(text) == 1:
            break
        def degree(a,b):
            result = a
            if b == 0:
                return 1
            elif b == 1:
                return a
            elif b > 1:
                return a * degree(a,b-1)
            elif b < 0:
                return 1 / (a * degree(a,abs(b+1)))

        n = float(text)
        m = int(input("Введите степень: ")) 
        print(f"Результат: {degree(n,m)}")

    except:
        print("Некорректный ввод")
        continue

print ("Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. ")
while True:
    try:
        text = (input("Введите первое число или наберите 'q' для выхода: "))
        if check_exit(text) == 1:
            break
        
        def Sum(a,b):
            if b > 0:
                return Sum(a+1,b-1)
            else:
                return a

        n = int(text)
        m = int(input("Введите второе число: ")) 
        print(Sum(n,m))
    except:
        print("Некорректный ввод")
        continue