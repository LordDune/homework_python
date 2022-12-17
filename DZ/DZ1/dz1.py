print("!!!Задача 2: Найдите сумму цифр трехзначного числа.")
print()
number = input("Введите трехзначное число: ")
def sum(number):
    try:
        if (int(number) < 0):
            number = number[1:len(number)]
        if (99 < int(number) < 1000):
            sum = 0
            for i in number:
                sum += int(i)
            return print(f'Результат: {sum}')
        else:
            return print('!!! Ошибка: введенное число должно быть трехзначным!')
    except:
        print("Некорректный ввод")

sum(number)
print()

print('!!!Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.\n\
    Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое \n\
    количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?')
print()
value = int(input("Введите число журавликов: "))

def count_numbers(value):
    if (value%6 !=0):
        return print('Ошибка: Количество журавликов должно быть кратно 6')
    else:
        value_p_s = value//6
        value_k = value-value_p_s*2
        if (value_k%10 > 4 or value_k%10 == 0 or 10 < value_k < 15):
            case = 'ов' 
        elif (5 > value_k%10 > 1):
            case = 'а'  
        return print(f'Результат: Катя сделала {value_k} журавлик{case}, а Петя и Сережа по {value_p_s}')
count_numbers(value)
print()

print("!!!Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд \n\
и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма \n\
первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. \n\
Вам требуется написать программу, которая проверяет счастливость билета.")
print()
numbers = input("Введите номер билета из 6 цифр: ")

def lucker_numbers(numbers):
    if ((len(numbers)) != 6):
        return print('Ошибка: номер билета должен состоять из 6 цифр')
    else:
        if (int(numbers[0]) + int(numbers[1]) + int(numbers[2]) == int(numbers[3]) + int(numbers[4]) + int(numbers[5])):
            return print("Результат: Билет счастливый!")
        else:
            return print("Результат: Билет несчастливый :-(")
lucker_numbers(numbers)
print()

print('!!!Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, \n\
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).')
print()
column = int(input("Введите количество долек шоколадки по горизонтали: "))
row = int(input("Введите количество долек шоколадки по вертикали: "))
count = int(input("Какое количество долек нужно отломить: "))

def break_chocolate(i, j, count):
        if (((count%row == 0) or (count%column == 0)) and count < row*column):
            return print('Результат: YES')
        else: 
            return print('Результат: NO')
break_chocolate(column, row, count)