from datetime import datetime
from datetime import timedelta
import requests, os
import json
from jinja2 import Environment, FileSystemLoader


# tabela musi być z dnia poprzedzającego wystawienie dokumentu.
# W przypadku gdzy dziś jest poniedziałek, to tabela musibyć z poprzedniego piątku
def date_to_query (offset = 1):
    weekend = timedelta(days=3)
    yesterday = timedelta(days=offset)
    if datetime.today().weekday() == 1:
        date_to_use = datetime.today() - weekend
    else:
        date_to_use = datetime.today() - yesterday

    date_to_use = date_to_use.strftime('%Y-%m-%d')
    return date_to_use


def currency_data(date_to_use):
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/' + date_to_use
    res = requests.get(url)
    res_is_ok = res.ok
    while res_is_ok is False:
        offset = 1
        date_to_use = date_to_query(offset)
        url = 'http://api.nbp.pl/api/exchangerates/tables/A/' + date_to_use
        res = requests.get(url)
        res_is_ok = res.ok
        offset += 1
    data = json.loads(res.text[1:-1])
    return data


def create_html_table(date_to_use,data):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('template.html')

    output= template.render(data=data, date_to_use=date_to_use )

    with open('temp_table.pdf', 'w') as file:
        file.write(output)

        
#=====main=======
date_to_use = date_to_query()
data = currency_data(date_to_use)
create_html_table(date_to_use,data)
os.startfile('temp_table.htm', "print")
