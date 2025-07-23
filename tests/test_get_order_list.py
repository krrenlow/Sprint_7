import requests
import allure

from data import urls, Flags


class TestGetOrderList:

    @allure.title('Получение списка заказов. Метод: /api/v1/orders')
    def test_order_list_success(self):
        response = requests.get(f'{urls.BASE_URL}{urls.GET_ORDER_LIST}')
        assert response.status_code == 200
        assert Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()
