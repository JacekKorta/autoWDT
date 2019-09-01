import asyncio, time, wdt_email
from pyppeteer import launch

eti = ("PL", "7811651261")


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('http://ec.europa.eu/taxation_customs/vies/vatResponse.html?locale=pl')
    await page.waitFor('#countryCombobox')
    await page.type('#countryCombobox', eti[0])
    await page.type('#number', eti[1])
    await page.click('#submit')
    time.sleep(5)
    await page.pdf(path='vies.pdf', format='A4')
    await browser.close()
    wdt_email.send_mail('vies', 'vies', 'jacek.korta@gmail.com', 'vies.pdf')

asyncio.get_event_loop().run_until_complete(main())


