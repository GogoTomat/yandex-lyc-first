# s = 'раз два три'
# print(s.split() == ['раз', 'два', 'три'])
# print('     one two  three  '.split() == ['one', 'two', 'three'])
# print('192.168.1.1'.split('.') == ['192', '168', '1', '1'])
# print(s.split('а') == ['р', 'з дв', ' три'])
# print('A##B##C'.split('##') == ['A', 'B', 'C'])
# print('####A##B######C####'.split('##') == ['', '', 'A', 'B', '', '', 'C', '', ''])

s = ['Тот', 'Кого', 'Нельзя', 'Называть']
# print(''.join(s) == 'ТотКогоНельзяНазывать')
# print(' '.join(s) == 'Тот Кого Нельзя Называть')
# print('-'.join(s) == 'Тот-Кого-Нельзя-Называть')
# print('! '.join(s) == 'Тот! Кого! Нельзя! Называть')

# message = input().split()
# secret_words = message[2::3]
# secret_message = ' '.join(secret_words)
# print(secret_message)

# squares = []
# for i in range(10):
#     squares.append(i ** 2)
# print(squares)

# squaresTwo = [i ** 2 for i in range(0, 10, 2)]
# print(*squaresTwo)

# print(['четное' if x % 2 == 0 else 'нечетное' for x in range(10)])
# print([i * j for i in range(3) for j in range(3)])

# a = [int(x) for x in '976 929 289 809 7677'.split()]
# print(a)
# evil, good = [int(x) for x in '666 777'.split()]
# print(evil, good, sep='\n')

# print(', '.join(str(i) + '^2=' + str(i ** 2) for i in range(1, 10))) 
n = int(input())
a = [i ** 2 for i in range(n)]
for x in a:
    print(x)

a = int(input().split())