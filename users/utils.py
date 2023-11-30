from random import random, choice


def create_token():
    return str(random())[2:]


def restore_password():
    pas = ''
    for x in range(8):
        pas = pas + choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    return pas
