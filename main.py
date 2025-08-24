"""Основная программа"""

#from src.masks import get_mask_account, get_mask_card_number
#from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

#card = input("Введите номер карты: ")
#account = input("Введите номер счёта: ")
#card_or_account = input("Введите название и номер карты или счёт: ")
#random_date = input("Введите дату: ")

#print(f"Замаскированный номер карты: {get_mask_card_number(card)}")
#print(f"Замаскированный номер счёта: {get_mask_account(account)}")
#print(f"Новая функция: {mask_account_card(card_or_account)}")
#print(f"А дата такая: {get_date(random_date)}")
"""Проверка условий Lab 10.1"""
somelist = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
some_state = input("Введите искомое значение state")
print(filter_by_state(somelist, some_state))
direct = input("Введите направление сортироки up/down: ")
print(sort_by_date(somelist, direct))