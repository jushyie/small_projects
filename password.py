import random
import string

def create_pw(n):
    chars = string.printable
    password = ""
    for _ in range(n):
        password += random.choice(chars)
    return password

def crack_pw(n, pw):
    chars = string.printable
    wrong = []
    while True:
        guess = ""
        for _ in range(n):
            guess += random.choice(chars)
        if guess != pw:
            wrong.append(guess)
        elif guess == pw:
            return guess

length = 3
pw = create_pw(length)
crack = crack_pw(length, pw)

    