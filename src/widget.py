"""Модуль для маскировки номеров карт, номеров счетов или получения даты"""

from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(card_or_account: str) -> str:
    words_list = card_or_account.split()
    stroka = ""
    if words_list[0] == "Visa":
        stroka = words_list[0] + " " + words_list[1] + " " + get_mask_card_number(words_list[2])
    elif words_list[0] == "Maestro":
        stroka = words_list[0] + " " + get_mask_card_number(words_list[1])
    else:
        stroka = words_list[0] + " " + get_mask_account(words_list[1])
    return stroka
