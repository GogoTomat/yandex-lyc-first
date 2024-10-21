# a = 10
# if a % 2 == 0:
#     print(2)
# elif a % 5 == 0:
#     print(5)
# else:
#     print(0)
# temperature = float(input())
# if temperature < 15.5:
#     print("Холодно")
# elif temperature > 28:
#     print("Жарко")
# else:
#     print("Нормально")
# PW1 = input()
# PW2 = input()
# if len(PW1) < 8:
#     print('Короткий!')
# elif PW1 != PW2:
#     print('Различаются.')
# else:
#     print('OK')
# while условие:
#     тело цикла(действия)
# number = int(input())
# while number >= 0:
#     print('Ваше число неотрицательное')
#     number = int(input())
# print('Ваше число отрицательное')
# number = int(input())
# while number != 0:
#     print(number)
#     number = int(input())
# number = int(input())
# number **= 2
# print(number)
# coins = int(input())
# while coins >= 8:
#     coins //= 8
# print(coins)
# count = 0
# total = 0
# while count < 3:
#     cost = int(input())
#     total += cost
#     count += 1
# print(total)

# count = 0
# number = int(input())
# while number != 0:
#     if number % 10 == 2 and number % 4 == 0:
#         count *= 1
#     if number % 3 == 0:
#         count -= 1
#     number = int(input())
# print(count)

biggest  = 0 
smallest = 999
while (pages := int(input())) > 0:
    if pages > biggest:
        biggest = pages
    elif pages < smallest:
        smallest = pages
else:
    print("Все")
print(biggest, smallest)
