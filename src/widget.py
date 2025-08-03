"""Модуль для маскировки номеров карт, номеров счетов или получения даты"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    words_list = card_or_account.split()
    mask_str = ""
    if words_list[0] == "Счет":
        mask_str = words_list[0] + " " + get_mask_account(words_list[1])
    else:
        mask_str = " ".join(words_list[:-1]) + " " + get_mask_card_number(words_list[-1])
    return mask_str


def get_date(some_date: str) -> str:
    date_in_russian = ".".join([some_date[8:10], some_date[5:7], some_date[:4]])
    return date_in_russian
