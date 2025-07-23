import requests
import allure
import pytest

import generators
from data import urls, ResponseBody, DataForLoginPayloadMissing


class TestLoginCourier:

    @allure.title('Успешная авторизация. Метод: /api/v1/courier/login')
    def test_login_courier_success(self, create_courier):
        courier_id, create_payload, login_payload = create_courier

        # Выполняем авторизацию под созданным курьером
        response_login = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', json=login_payload)
        assert response_login.status_code == 200
        assert 'id' in response_login.json()

    @allure.title('Попытка входа с неправильными авторизационными данными. Метод: /api/v1/courier/login')
    def test_login_courier_invalid_data_shows_error(self):
        # Пробуем залогиниться со сгенерированными данными без создания курьера
        login_payload = {
            'login': generators.generate_login(),
            'password': generators.generate_password()
        }
        response = requests.post(f'{urls.BASE_URL}{urls.LOGIN_COURIER}', json=login_payload)
        assert response.status_code == 404
        assert response.json().get('message') == ResponseBody.COURIER_ACCOUNT_NOT_FOUND['message']

    @allure.title('Попытка входа без заполнения обязательного параметра. Метод: /api/v1/courier/login')
    @pytest.mark.parametrize('payload_missing', DataForLoginPayloadMissing.login_data)
    def test_login_courier_missing_required_field_shows_error(self, payload_missing):
        # Передаём неполный набор параметров
        response = requests.post( f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=payload_missing, timeout=10)
        assert response.status_code == 400
        assert response.json().get('message') == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA['message']
