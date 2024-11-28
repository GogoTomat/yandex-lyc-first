# n = int(input())
# pupils = []
# for i in range(n):
#     pupils.append(input())
# # pupils = list(map(int, input().split()))
# for pupil in pupils:
#     print(pupil)
# print()
# for pupil in pupils:
#     if pupil[-1] in ['4', '5']:
#         print(pupil)

# card = ('7', 'пик')
# empty = ()
# t = (18,)
# print(len(card), card[0], type(card), t + card)

# print((1, 2) == (1, 3))
# print((1, 2) < (1, 3))
# print((1, 2) < (1, 1))
# print((1, 2) <= (1, 'fdsfdsf'))

# a = {(1, 2, 3), (1, 3, 4)}
# print(a)
# a, b = b, a
# n, s = 10, 'h'
# b = 10
# s = 'h'
# cards = [('7', 'pick'), ('Q', 'tref'), ('T', 'bubna')]
# value, suit = cards[0], True
# print(value)
# print(suit)
# n = int(input())
# t1 = t2 = t3 = 1
# for i in range(n):
#     print(t1, end=' ')
#     t1, t2, t3 = t2, t3, t1 + t2 + t3
# O(n)
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(*a)
# sigma = ('adfsf', 123)
# a = list(sigma)
# print(a)
a = [1, 2, 3, 4, 5, 5, 1, 2, 3]
print(len(set(a)))