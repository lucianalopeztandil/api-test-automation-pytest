import pytest
import requests
from BackendAutomation.resources.config import BASE_URL, ADD_BOOK_ENDPOINT
from BackendAutomation.resources.payloads import add_book_payload

@pytest.fixture(scope="module")
def book_id():
    response = requests.post(
        url=f"{BASE_URL}{ADD_BOOK_ENDPOINT}",
        json=add_book_payload()
    )

    assert response.status_code == 200
    return response.json()['ID']
