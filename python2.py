"""telegram bot which works with NBU API"""

import requests
import datetime
import json
def currency_rate1(update, context):
    global message
    chat = update.effective_chat
currency_code = "USD", "EUR", "CZK", "CHF"
last_year_currency_code = currency_code
time = int(input("Enter time: ")
l = ["USD", "EUR", "CZK", "CHF"]
if currency_code in l:
    print(currency_code)
else:
    try:
        currency_code = "123"
        time = "abc"
    except TypeError:
        print("You don't need a number in currency_code")
        print("You don't need a letter in time")

currency_rate1 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                              f'{currency_code}&date=20220313&json').json()


currency_rate2 = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                              f'{currency_code}&date=20210313&json').json()
rate = currency_rate1[0]['rate']
date1 = 20220313
date2 = 20210313
data = {"currency code": currency_code, "date1": date1, "date2": date2,  "rate": rate,
                "difference": currency_rate1 - currency_rate2, "date": datetime.date, time: time}
def write_to_file(message):
    with open("f.json", "a") as f:
        f.write(json.dumps(data))
def get_details_from_api(currency_code, date):
    api = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=")
                 f"{currency_code}&date={date}&json").json
    print(api)
def create_2_dates():
    date1 = datetime.datetime.now()
    date2 = date1 - 1
    print(date1, date2)

def currency_rate1(update, context):
    global message
    chat = update.effective_chat
    currency_code = update.message.text
    create_2_dates()


date1 = 20220313
date2 = 20210313
def create_to_json(currency_code, date, rate):
    currency_rate1 = create_to_json(currency_code, date1)
    currency_rate2 = create_to_json(currency_code, date2)
    data = {"currency code": currency_code, "date1": date1, "date2": date2 "rate": rate,
                "difference": currency_rate1 - currency_rate2, "date1": date1, time: time}
    d = json.dumps(data)
    print(d)
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL'):
        currency_rate1 = create_to_json(currency_code, date1)
        currency_rate2 = create_to_json(currency_code, date2)
        my_memory = [{'currency': currency_code[0]['cc'], 'current rate': currency_rate1[0]['cc'], 'rate of the last year': currency_rate2[0]['cc'], 'difference': currency_rate1 - currency_rate2[0]['rate'], "date1": 20220313, "date2": 20210313, "time": time}]
        def prepare_message_for_json_file(currency_rate1, currency_rate2, my_memory):
            my_memory = [{'currency': currency_code[0]['cc'], 'current rate': currency_rate1[0]['cc'], 'rate of the last year': currency_rate2[0]['cc'], 'difference': currency_rate1 - currency_rate2[0]['rate'], "date1": 20220313, "date2": 20210313, "time": time}]
        return my_memory
rate = currency_rate1[0]['rate']
currency_difference = currency_rate1 - currency_rate2
message = f'{currency_code} rate: {rate} UAH'
create_to_json(currency_code, date, rate)
def load_file_currency(currency):
    with open("accounts1.txt") as f:
        json.load = load_file_currency
        json.load["information"].append(currency)
        with open("accounts1.txt", "w") as f1:
            json.dump(load_file_currency, f1, ensure_ascii=False, indent=2)
            print(load_file_currency())
            (create_to_json(currency_code, date, rate)
            rate = currency_rate1[0]['rate']
            message = f'{currency_code} rate: {rate} UAH'
            message1 = f'{currency_code}'
