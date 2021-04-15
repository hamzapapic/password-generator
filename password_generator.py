import random
import string
def password_generator(simboli,cifre,k):
    slova = string.ascii_letters
    if simboli:
        slova += string.punctuation
    if cifre:
        slova += string.digits
    return ''.join(random.choices(slova,k=k))
if __name__ == '__main__':
    print(password_generator(True,False,20))