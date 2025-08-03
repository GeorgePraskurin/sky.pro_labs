"""Основная программа"""

from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

#card = input("Введите номер карты")
#account = input("Введите номер счёта")
card_or_account = input("Введите название и номер карты или счёт")

#print(f"Замаскированный номер карты: {get_mask_card_number(card)}")
#print(f"Замаскированный номер счёта: {get_mask_account(account)}")
print(f"Новая функция: {mask_account_card(card_or_account)}")
