import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def get_dates(session, year, month, day):
    async with session.post('https://www.ashesh.com.np/linkdate-converter.php', data={
        'yeare': year,
        'month': month,
        'day': day,
        'submit': 'convert'
    }) as response:
        return await response.text()
        


async def get_all_dates(session, dates):
    tasks = []
    for date in dates:
        task = asyncio.create_task(
            get_dates(session, date[0], date[1], date[2]))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def main(dates):
    async with aiohttp.ClientSession() as session:
        results = await get_all_dates(session, dates)
        return results


def parse(results):
    dates = []
    for result in results:
        soup = BeautifulSoup(result, 'lxml')
        dates.append((soup.select(".inner")[1].text)[5:])
    return dates 

""" 

Use this function to get the nepali dates
dates = [(year, month, day), (year, month, day), ...] in AD

"""

def get_nepali_dates(dates):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main(dates))
    return (parse((results)))