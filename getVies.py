import time
from pyppeteer import launch


async def get_vies(country_code, vat_number):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('http://ec.europa.eu/taxation_customs/vies/vatResponse.html?locale=pl')
    await page.waitFor('#countryCombobox')
    await page.type('#countryCombobox', country_code)
    await page.type('#number', vat_number)
    await page.click('#submit')
    print('submit')
    time.sleep(5)
    await page.pdf(path='vies.pdf', format='A4')
    time.sleep(2)
    await browser.close()
