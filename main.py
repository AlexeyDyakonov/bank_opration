from settings import OPERATIONS_PATH, COUNT_OPERATION
from src.functions import (read_json,
                           convert_date,
                           get_executed_operations,
                           sort_operations,
                           convert_payment,
                           get_last_operations
                           )



def main():
    list_operations = read_json(OPERATIONS_PATH)
    executed_operations = get_executed_operations(list_operations)
    sort_date_operation = sort_operations(executed_operations)
    last_sort_operation = get_last_operations(sort_date_operation, COUNT_OPERATION)

    for operation in last_sort_operation:
        print(f"{convert_date(operation['date'])} {operation['description']}\n"
              f"{convert_payment(operation['from'])} -> {convert_payment(operation['to'])}\n"
              f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
              )
    test_datе = [
        {"date": "2018-08-19T04:27:37.904916"},
        {"date": "2018-07-11T02:26:18.671407"},
        {"date": "2019-09-11T17:30:34.445824"}]
    print(sort_operations(test_datе))

if __name__ == '__main__':
    main()
