import aiohttp
import asyncio


async def fetch(session, url):
    print('发送请求')
    async with session.get(url, veryfy_ssl=False) as response:
        content = await response.conetent.read()
        file_name = url
        with open(file_name, 'wb') as file_object:
            file_object.write(content)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            '1',
            '2',
            '3'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())