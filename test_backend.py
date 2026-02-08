import requests
import allure

from BackendAutomation.resources.config import BASE_URL, GET_BOOK_ENDPOINT, DELETE_BOOK_ENDPOINT
from BackendAutomation.resources.payloads import delete_book_payload


@allure.title("Return book")
@allure.description("Return data of a book via API")
def test_get_book(book_id):
    with allure.step("Send get request to get a book"):
        response = requests.get(
            url=f"{BASE_URL}{GET_BOOK_ENDPOINT}",
            params={'ID': book_id}
        )

    with allure.step("Validate response status code"):
        assert response.status_code == 200
        print(response.json())

@allure.title("Delete a book via API")
@allure.description("Validates that a book can be deleted successfully")
def test_delete_book(book_id):
    with allure.step("Send POST request to delete a book"):
        response = requests.delete(
            url=f"{BASE_URL}{DELETE_BOOK_ENDPOINT}",
            json=delete_book_payload(book_id)
        )

    with allure.step("Validate response status code"):
        assert response.status_code == 200
        print(response.json())
