from datetime import datetime
import json


def read_json(path):
    """Чтение JSON файла"""
    with open(path, 'r', encoding="utf8") as json_file:
        return json.load(json_file)


def convert_date(date):
    """
    Конвертирует дату
    """
    date_format = date.split('T')[0]
    return datetime.strptime(date_format, '%Y-%m-%d').date().strftime('%d.%m.%Y')


def convert_payment(card):
    """
    Конвертирует счет
    """
    if 'Счет' in card:
        return card[:4] + ' **' + card[-4:]
    else:
        name = card[:-17]
        nums = card[-16:]
        nums = nums.replace(card[-10:-4], '******')
        format_nums = ''
        for i in range(0, len(nums), 4):
            format_nums += nums[i:i + 4] + ' '
        return name + ' ' + format_nums


def get_executed_operations(operations):
    """Успешные операции"""
    executed_operations = []
    for operation in operations:
        if not operation:
            continue
        else:
            if operation['state'] == "EXECUTED" and "from" in operation:
                executed_operations.append(operation)
    return executed_operations


def sort_operations(executed_operations):
    """Сортировка по дате"""
    sort_date = []
    for executed_operation in executed_operations:
        sort_date.append(executed_operation)
        sorted_list = sorted(sort_date, key=lambda x: x['date'], reverse=True)
    return sorted_list


def get_last_operations(operations, count):
    """count последних успешных операций"""
    return operations[:count]
