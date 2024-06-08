from settings import TESTS_OPERATIONS_PATH
from src.functions import (
    read_json,
    convert_date,
    convert_payment,
    get_executed_operations,
    sort_operations,
    get_last_operations
)

test_EXECUTED = [
    {"state": "EXECUTED", "from": "72321"},
    {"state": "123", "from": "12321"},
    {"state": "EXECUTED", "from": "12321"},
]

test_date = [
    {"date": "2018-08-19T04:27:37.904916"},
    {"date": "2018-07-11T02:26:18.671407"},
    {"date": "2019-09-11T17:30:34.445824"},
]


def test__read_json():
    operations = read_json(TESTS_OPERATIONS_PATH)
    assert len(operations) == 3
    assert isinstance(operations, list)
    assert isinstance(operations[0], dict)


def test__convert_date():
    assert convert_date('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert convert_date('2019-03-23T01:09:46.296404') == '23.03.2019'
    assert convert_date('2019-03-25T01:09:46.296404') == '25.03.2019'


def test__convert_payment():
    assert convert_payment('Счет 19708645243227258542') == 'Счет **8542'
    assert convert_payment('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658 '


def test__get_executed_operations():
    assert get_executed_operations(test_EXECUTED) == [
        {"state": "EXECUTED", "from": "72321"},
        {"state": "EXECUTED", "from": "12321"},
    ]


def test__sort_operations():
    assert sort_operations(test_date) == [
        {"date": "2019-09-11T17:30:34.445824"},
        {"date": "2018-08-19T04:27:37.904916"},
        {"date": "2018-07-11T02:26:18.671407"}
    ]


def test__get_last_operations():
    assert get_last_operations(test_date, 1) == [
        {"date": "2018-08-19T04:27:37.904916"}
    ]
