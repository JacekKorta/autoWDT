import asyncio, time, shelve, os
from getVies import get_vies
import nbpTable

customer_code_input = input('podaj kod kontrachenta: ').upper()

shelve_file = shelve.open('customer_db')
customer_c_code, customer_vat_num = shelve_file.get(customer_code_input, 'W bazie nie ma takiego klienta')
shelve_file.close()

asyncio.get_event_loop().run_until_complete(get_vies(customer_c_code, customer_vat_num))
os.startfile("vies.pdf", "print")
print('printing')
time.sleep(2)

date_to_use = nbpTable.date_to_query()
data, date_to_use = nbpTable.currency_data(date_to_use)
nbpTable.create_html_table(date_to_use, data)
os.startfile('temp_table.htm', "print")

input('Wcisnij Enter, aby zakończyć')
