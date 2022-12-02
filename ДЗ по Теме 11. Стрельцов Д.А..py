#!/usr/bin/env python
# coding: utf-8

# In[4]:





# In[21]:


import aiohttp
import asyncio
import time


async def get_page(session, url):
    async with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
    return data


if __name__ == '__main__':
    urls = [
               "https://www.jython.org",
               "https://python.org/",
           ] * 80
    start_time = time.time()
    get_all(urls)
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} in {duration} seconds")

results = asyncio.run(main(urls))
print(results)


# In[ ]:




