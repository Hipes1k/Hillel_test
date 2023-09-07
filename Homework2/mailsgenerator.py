from faker import Faker
import random


servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
tlds = ['.com', '.in', '.gov', '.ac.in', '.net', '.org']


def domain_generator():
    """Функция генерации рандомного домена

    :return: Возвращает строку с готовым доменом
    """
    servpos = random.randint(0, len(servers) - 1)
    tldpos = random.randint(0, len(tlds) - 1)

    return servers[servpos] + tlds[tldpos]



def fake_name_generator():
    """Функция генерации рандомного имени, фамилии

    :return: Возвращает список из рандомно сгенерированных имен
    """
    fake = Faker()
    lst = []
    for _ in range(100):
        lst.append(fake.name())
    return lst

fake_names = fake_name_generator()

def name_surname_join():
    """Функция для удаления пробела между именами и фамилиями

    :return: Возвращает список имен, фамилий без пробелов
    """
    lst2 = []
    while True:
        for i in fake_names:
            i_split = i.split()
            i_join = ''.join(i_split)
            lst2.append(i_join)
        return lst2

joined_list = name_surname_join()

def creating_mail():
    """Функция для создания email адреса

    :return: Возвращает готовый email
    """
    ready_gmail = []
    while True:
        for names in joined_list:
            ready_gmail.append(names+str(random.randint(100, 99999))+domain_generator())
        return ready_gmail

ready_mails_list = creating_mail()


def make_dict():
    """Функция для создания словаря имя:электронный ящик

    :return: Возвращает готовый словарь
    """
    res = dict(zip(fake_names, ready_mails_list))
    return res
