from datetime import datetime, timedelta
import requests
import json
from jinja2 import Environment, FileSystemLoader

# tabela musi być z dnia poprzedzającego wystawienie dokumentu.
# W przypadku gdzy dziś jest niedziela lub poniedziałek, to tabela musibyć z poprzedniego piątku
def date_to_query(offset=1):
    if datetime.today().weekday() == 1:
        days_offset = timedelta(days=3)
    elif datetime.today().weekday() == 7:
        days_offset = timedelta(days=2)
    else:
        days_offset = timedelta(days=offset)
    date_to_use = datetime.today() - days_offset
    date_to_use = date_to_use.strftime('%Y-%m-%d')
    return date_to_use


def currency_data(date_to_use):
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/' + date_to_use
    res = requests.get(url)
    res_is_ok = res.ok
    offset = 1
    while res_is_ok is False:
        # W przypadku gdy zapytanie jest robione po świecie wypadającym w środku tygodnia, program cofa się
        # do najbliższego dnia roboczego.
        date_to_use = date_to_query(offset)
        url = 'http://api.nbp.pl/api/exchangerates/tables/A/' + date_to_use
        res = requests.get(url)
        res_is_ok = res.ok
        offset += 1
    data = json.loads(res.text[1:-1])
    return data, date_to_use


def create_html_table(date_to_use, data):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('template.html')
    output = template.render(data=data, date_to_use=date_to_use)
    with open('temp_table.htm', 'w') as file:
        file.write(output)

