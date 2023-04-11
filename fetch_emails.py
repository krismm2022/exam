import asyncio
import aiohttp

async def fetch_emails(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            comments = await response.json()
            emails = [comment["email"] for comment in comments]
            return emails
        else:
            return []

# data saved in ./emails.txt
async def save_emails(emails):
    with open("emails.txt", "a") as f:
        for email in emails:
            f.write(email + "\n")

async def main():
        async with aiohttp.ClientSession() as session:
            for idx in range(1,100):
                url = "https://jsonplaceholder.typicode.com/posts/{}/comments".format(idx)
                tasks = []
                
                task = asyncio.ensure_future(fetch_emails(session, url))
                tasks.append(task)
                responses = await asyncio.gather(*tasks)
                for response in responses:
                    await save_emails(response)

if __name__ == "__main__":
    import time
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time:.2f} seconds")
