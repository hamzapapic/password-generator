import string
import random
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
k = int(input("Unesite duzinu vase sifre: "))
a = input("Da li zelite simbole u vasoj sifri: ")
b = input("Da li zelite cifre u vasoj sifri: ")
slova = string.ascii_letters
if a:
    slova += string.digits
if b:
    slova += string.punctuation
for i in random.choices(slova,k=k):
    print(i, sep='',end= '')