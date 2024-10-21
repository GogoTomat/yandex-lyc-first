# total = 0
# print('Вводите цены; для остановки введите -1.')
# price = float(input())
# while price > 0:
#     total += price
#     price = float(input())
# print('Общая стоимость равна', total)

# print('Добро пожаловать в интернет-банк!')
# print('У нас фантастические процентные ставки!')
# print('Для вкладов до 10 тысяч ₽ включительно прибыль составит 10%,')
# print('для вкладов на сумму до 100 тысяч включительно - 20%,')
# print('для более 100 тысяч - 30%!')
# print('На какую сумму желаете сделать вклад?')
# money = float(input())
# if money <= 10000:
#     money *= 1.1
# elif money <= 100000:
#     money *= 1.2
# elif money > 100000:
#     money *= 1.3
# print('Вы получаете', money, '₽, поздравляем!')

# count = 0
# number = int(input())
# while number != 0:
#     if number % 10 == 2 and number % 4 == 0:
#         count += 1
#     number = int(input())
# print('Количество искомых чисел:', count)

# prev1 = 1
# prev2 = 1
# now = 2
# while prev1 <= int(input()):
#     print(now)
#     now = now + prev1
#     prev1 = prev2
#     prev2 = now


# limit = int(input())
# old_fib = 1  # мы помним два самых свежих числа Фибоначчи: более старое и более новое
# current_fib = 1  # последовательность начинается с двух единиц
# while old_fib <= limit:
#     print(old_fib)  # более старое из двух - именно то, которое выводится на экран
#     new_fib = old_fib + current_fib  # сохраняем следующее число в отдельную переменую
#     old_fib = current_fib  # всё, теперь старое число Фибоначчи использовано, можно его забыть;
#     # "новым старым" становится бывшее новое
#
#     current_fib = new_fib  # следующее число становится "новым новым"


height = int(input())
count = 0
min = 999
max = 1
while height != '!':
    height = int(height)
    if height < min:
        min = height
    elif height > max:
        max = height
    if height >= 150 and height <= 190:
        count += 1
    height = input()
print(f"""{count}
{min} {max}""")