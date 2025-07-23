import pytest
import requests
import generators
from data import urls

@pytest.fixture
def courier_creds():
    login = generators.generate_login()
    password = generators.generate_password()
    first_name = generators.generate_firstname()

    create_payload = {
        'login': login,
        'password': password,
        'first_name': first_name
    }

    login_payload = {
        'login': login,
        'password': password
    }

    yield create_payload, login_payload

    # Проходим авторизацию и извлекаем "ID"
    response_login = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', json=login_payload)
    courier_id = response_login.json().get('id')

    # Удаляем курьера
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER}{courier_id}')

@pytest.fixture
def create_courier(courier_creds):
    create_payload, login_payload = courier_creds

    # Создаем нового курьера
    requests.post(f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=create_payload)

    # Проходим авторизацию и извлекаем нового курьера по "ID"
    response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', json=login_payload)
    courier_id = response.json().get('id')

    yield courier_id, create_payload, login_payload

    # Удаляем созданного курьера
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_COURIER}{courier_id}')
