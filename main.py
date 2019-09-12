import asyncio, time, shelve, os
from pyppeteer import launch

customer_code_input = input('podaj kod kontrachenta: ').upper()

shelve_file = shelve.open('customer_db')
customer = shelve_file.get(customer_code_input, 'W bazie nie ma takiego klienta')
shelve_file.close()

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('http://ec.europa.eu/taxation_customs/vies/vatResponse.html?locale=pl')
    await page.waitFor('#countryCombobox')
    await page.type('#countryCombobox', customer[0])
    await page.type('#number', customer[1])
    await page.click('#submit')
    print('submit')
    time.sleep(5)
<<<<<<< HEAD
    await page.pdf({'path': 'vies.pdf'})
    #os.startfile("vies.pdf", "print")
    print('printing')
    time.sleep(2)
=======
    await page.pdf(path='vies.pdf', format='A4')
    await browser.close()
    os.startfile("vies.pdf", "print")
>>>>>>> 13506306228381dc70ea475c13163d62e63cab70

asyncio.get_event_loop().run_until_complete(main())

input('Wcisnij Enter, aby zakończyć')


