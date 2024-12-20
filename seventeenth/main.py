# dictonary = { key : value, 
#              key : value}
# users = {1 : 'Alex', 2 : "Paul", 3 : "Kirill"}
# mails = {"sigma@gmail.com" : "Alex", "sigma2@yandex.ru" : "Paul", "sigma3@outlook.com" : "Kirill"}
# aboba = {1 : "Alex", True : "Paul", "sigma" : "kirill"}
# obj = dict()
user_list = [[1, 'dsfsdf'], ['dsfsdf', 'sdfsdf'], [34234, 'sfdfsdf']]
user_dict = dict(user_list)
# print(user_dict)
# # print(user_dict)
# # print(user_dict['dsfsdf'])
# # user_dict[66.6] = "Alex"
# # print(*user_dict)
# aboba = user_dict.copy()
# print(aboba)
# aboba.update(user_dict)
# print(aboba)
# for key, value in user_dict.items():
#     print(key)
#     print(value)
# for key in user_dict:
#     print(key, user_dict[key])
for key in user_dict.keys():
    print(key)