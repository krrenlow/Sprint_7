import requests
import allure
import pytest

from data import urls, ResponseBody, DataForRegistration


class TestCreateNewCourier:

    @allure.title('Создание нового курьера проходит успешно. Метод: /api/v1/courier')
    def test_create_courier_success(self, courier_creds):
        create_payload, login_payload = courier_creds

        # Создаём нового курьера
        response_create = requests.post(f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=create_payload)
        assert response_create.status_code == 201
        assert response_create.json() == ResponseBody.COURIER_CREATION_SUCCESS

    @allure.title('Попытка создать уже двух одинаковых курьеров. Метод: /api/v1/courier')
    def test_create_duplicate_courier_shows_error(self, courier_creds):
        create_payload, login_payload = courier_creds

        # Создаём нового курьера
        response_create = requests.post(f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=create_payload)
        assert response_create.status_code == 201
        assert response_create.json() == ResponseBody.COURIER_CREATION_SUCCESS

        # Пытаемся создать курьера который был предсоздан ранее
        response_create_2 = requests.post(f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=create_payload)
        assert response_create_2.status_code == 409
        assert response_create_2.json().get('message') == ResponseBody.COURIER_NAME_ALREADY_EXIST['message']

    @allure.title('Попытка создать нового курьера без передачи обязательного параметра. Метод: /api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_create_courier_missing_required_field_shows_error(self, data_setup):
        # Передаем неполный набор параметров
        response = requests.post(f'{urls.BASE_URL}{urls.CREATE_COURIER}', json=data_setup)
        assert response.status_code == 400
        assert response.json().get('message') == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA['message']
