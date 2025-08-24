def filter_by_state(list_of_dicts: list, filter_state = "EXECUTED") -> list:
    """Фильтрация по элементу словаря state"""
    filteres_list = []
    for i in list_of_dicts:
        if i["state"] == filter_state:
            filteres_list.append(i)
    return filteres_list

def sort_by_date(list_of_dicts: list, direction: str) -> list:
    """Сортировка по дате"""
    sorted_list = []
    list_of_date = []
    for i in list_of_dicts:
        list_of_date.append(i["date"])
    if direction == "down":
        list_of_date.sort(reverse=True)
    else:
        list_of_date.sort()
    for i in range(len(list_of_dicts)):
        for j in list_of_dicts:
            if j["date"] == list_of_date[i]:
                sorted_list.append(j)
    return sorted_list

