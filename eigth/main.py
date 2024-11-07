# # k = int(input())
# # for i in range(1, k + 1):
# #     for j in range(1, 10):
# #         print(i, '*', j, '=', i * j, sep='', end='\t')
# #     print()

# k = int(input())
# for j in range(1, 10):
#     if j == k:
#         continue
#     for i in range(1, 10):
#         if i == k:
#             break
#         print(i, '*', j, '=', j * i, sep='', end='\t')
#     print()

# print('Тренажер по вводу палиндрома:')
# while True:
#     print('Введите число палиндром:')
#     number = n = int(input())
#     reverse = 0
#     while n > 0:
#         reverse = reverse * 10 + n % 10
#         n //= 10
#     if number == reverse:
#         print('Вы ввели палиндром! Программа остановлена.')
#         break
#     print('Введенное число не палиндром, попробуйте еще раз.')

n = int(input())
k = 1
line = 1
while k <= n:
    for i in range(line):
        print(k, end=" ")
        k += 1
        if k > n:
            break
    line += 1
    print()