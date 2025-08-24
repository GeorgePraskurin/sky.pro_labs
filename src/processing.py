def filter_by_state(list_of_dicts: list, filter_state = "EXECUTED") -> list:
    """Фильтрация по элементу словаря state"""
    filteres_list = []
    for i in list_of_dicts:
        if i["state"] == filter_state:
            filteres_list.append(i)
    return filteres_list

def sort_by_date():
    """Сортировка по дате"""
    pass

