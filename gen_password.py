import random

chars = 'abcdefghijklnopqrstuvwxyz'
chars_0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars_1 = '0123456789'
chars_2 = '+-=/*!?&$#%@<>'

number = int(input('Количество паролей?'+ "\n"))
length = int(input('Длина пароля?'+ "\n"))

ch_0 = int(input('Минимальное количество прописных букв:'+ "\n"))
ch_1 = int(input('Минимальное количество чисел:'+ "\n"))
ch_2 = int(input('Минимальное количество символов:'+ "\n"))

f = open('password.txt', 'w')

if ch_0 > 0: chars += chars_0
if ch_1 > 0: chars += chars_1
if ch_2 > 0: chars += chars_2

for n in range(number):
    password =''

    for i in range(ch_0):
        password += random.choice(chars_0)

    for i in range(ch_1):
        password += random.choice(chars_1)

    for i in range(ch_2):
        password += random.choice(chars_2)

    for i in range(length - ch_0 - ch_1 - ch_2):
        password += random.choice(chars)

    str(random.shuffle(list(password)))    
    print(password)
    f.write(password + '\n')

f.close()