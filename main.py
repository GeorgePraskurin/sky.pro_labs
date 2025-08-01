"""Основная программа"""

from src.masks import get_mask_account, get_mask_card_number

card = input("Введите номер карты")
account = input("Введите номер счёта")

print(f"Замаскированный номер карты: {get_mask_card_number(card)}")
print(f"Замаскированный номер счёта: {get_mask_account(account)}")
