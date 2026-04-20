import random

def rdata_for_good_reg():
    new_name = f'Karlos{random.randint(100,999)}'
    new_email = f'karlos{random.randint(100,999)}@mail.ru'
    new_password = f'karlos{random.randint(100,999)}'
    return new_name, new_email, new_password

def rdata_for_badpass_reg():
    new_name = f'Karlos{random.randint(100,999)}'
    new_email = f'karlos{random.randint(100,999)}@mail.ru'
    new_password = f'k{random.randint(100,999)}'
    return new_name, new_email, new_password