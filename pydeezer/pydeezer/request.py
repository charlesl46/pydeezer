import requests
from urllib.parse import urljoin

BASE_URL = "https://api.deezer.com"


def get_full_url(endpoint: str):
    return urljoin(BASE_URL, endpoint)


def control(response: requests.Response) -> dict:
    if not response.ok:
        raise ConnectionError(
            f"Couldn't make request to {response.url} ({response.status_code} - {response.reason})"
        )

    if response.json().get("error"):
        raise Exception(f"Request to {response.url} returned an error ({response.json().get('error').get('message')})")

    return response.json()


def get(endpoint: str):
    url = get_full_url(endpoint)
    print(f"making get request to {url}")
    response = requests.get(url)
    return control(response)
