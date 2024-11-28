# primes = [2, 3, 5, 7, 11]
# print(primes)
# emptyOne = []
# emptyTwo = list()
# print([2, 3] * 4)
# l = [0] * 100
# print(primes[0] + primes[1])
# print(primes[5])
# primes.append(13)
# print(primes)
# my_list = [1, 2, 3]
# # another_list = [4, 5, 6]
# # str = "привет"
# # sets = {'g', 'f', 'z'}
# # my_list.extend(sets)
# # print(my_list)
# # my_list[0] = 3
# # print(my_list)
# print(len(primes))
# primes += [23, 29]
# print(primes)
# if 1 in primes:
#     print(3)
# n = int(input())
# words = []
# for i in range(n):
#     word = input()
#     words.append(word)
# letter_number = int(input()) - 1
# for i in range(n):
#     word = words[i]
#     if letter_number < len(word):
#         print(word[letter_number], end='')
# n = int(input())
# phrases = []
# for i in range(n):
#     phrase = input()
#     phrases.append(phrase)
# n_announce = int(input())
# ann = []
# for i in range(n_announce): len(ann)
#     ann_number = int(input()) - 1
#     ann.append(phrases[ann_number])
# for i in range(n_announce):
#     print(ann[i])

# texts = []
# for i in range(int(input())):
#     texts.append(input())
# for i in range(int(input())):
#     print(texts[(int(input())) - 1])
# nums = [1, 2, 3]
# for num in nums:
#     print(num ** 2)
# a = []
# n = 10
# for i in range(n):
#     a.append(input())
# months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль',
#           'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
# spring = months[2:5]
# months[5:8] = ['sdfds', 'sdfdsf', 'sdfds']
# for month in spring:
#     print(month)
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# p = int(input())
# q = int(input())
# res = 0
# for num in a[p - 1:q]:
#     res += num
# print(num)
a = [1, 2, 3, 4, 5, 6,]
del(a[::2])
print(a)