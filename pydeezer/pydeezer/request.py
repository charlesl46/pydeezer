import requests
from urllib.parse import urljoin
import aiohttp
import asyncio

BASE_URL = "https://api.deezer.com"


def get_full_url(endpoint: str):
    return urljoin(BASE_URL, endpoint)


def control(response: requests.Response) -> dict:
    if not response.ok:
        raise ConnectionError(
            f"Couldn't make request to {response.url} ({response.status_code} - {response.reason})"
        )

    if response.json().get("error"):
        raise Exception(
            f"Request to {response.url} returned an error ({response.json().get('error').get('message')})"
        )

    return response.json()


async def control_async(response: aiohttp.ClientResponse):
    if not response.ok:
        raise ConnectionError(
            f"Couldn't make request to {response.url} ({response.status_code} - {response.reason})"
        )

    json = await response.json()

    if json.get("error"):
        raise Exception(
            f"Request to {response.url} returned an error ({response.json().get('error').get('message')})"
        )

    return json


async def get_async(urls: list[str]):

    async def fetch(session: aiohttp.ClientSession, url):
        async with session.get(get_full_url(url)) as response:
            return await control_async(response)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

    return responses


def get(endpoint: str):
    url = get_full_url(endpoint)
    print(f"making get request to {url}")
    response = requests.get(url)
    return control(response)
