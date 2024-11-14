# size = int(input())
# firat_letter_code = ord('A')
# for row_index in range(size, 0, -1):
#     for column_index in range(size):
#         letter = chr(firat_letter_code + column_index)
#         print(letter + str(row_index), end=' ')
#     print()

# username = str(input())
# for character in username:
#     if not ('0' <= character <= '9' or 'a' <= character <= 'z' or character == '_'):
#         print(f'Неверный символ: {character}')
#         break
# else:
#     print('OK')

# line = input()
# count = 0
# for i in line:
#     if (ord(i) < 123 and ord(i) > 96) or (ord(i) > 47 and ord(i) < 58) or i == '_':
#         count += 1
#     else:
#         print('Неверный символ:', i)
#         break
# if count == len(line):
#     print("OK")

# ticket = str(input())
# odd = even = 0
# for i in range(0, len(ticket), 2):
#     odd += int(ticket[i])
# for i in range(1, len(ticket), 2):
#     even == int(ticket[i])
# print(odd == even)

# text = 'Hello, world!'
# # print(text[:5])
# print(text[-1:])
# number = str(input())
# odd = even = 0
# for i in number[::2]:
#     odd += int(i)
# for n in number[1::2]:
#     even += int(n)
# print(odd = even)
# string = 'Python'
# print(string[2:1000])
# print(string[1000:])
# text = 'бел хлеб'
# text_reversed = text[::-1]
# print(text == text_reversed)
# max_word = min_word = word = input()
# while word != 'стоп':
#     if len(word) < len(min_word):
#         min_word = word
#     if len(word) > len(max_word):
#         max_word = word
#     word = input()

# if set(min_word) < set(max_word):
#     print('Да')
# else:
#     print('Нет')
limit = int(input())
news_count = int(input())
for _ in range(news_count):
    title = input()
    if len(title) > limit:
        title = title[:limit - 3] + '...'
    print(title)