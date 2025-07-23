import requests
import allure
import pytest

from data import urls, Flags, DataForOrder


class TestCreateOrder:

    @allure.title('Успешное создание заказа со всеми вариантами цветов. Метод: /api/v1/orders')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_make_order_various_colors(self, scooter_color):
        order_payload = DataForOrder.order_payload
        order_payload['color'] = scooter_color
        response = requests.post(f'{urls.BASE_URL}{urls.CREATE_ORDER}', json=order_payload)
        assert response.status_code == 201
        assert Flags.SUCCESSFUL_ORDER_CREATION in response.json()
        requests.put(f'{urls.BASE_URL}{urls.CANCEL_ORDER}{response.json()["track"]}')
