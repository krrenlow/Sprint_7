import generators

class urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = '/api/v1/courier'
    LOGIN_COURIER = '/api/v1/courier/login'
    DELETE_COURIER = '/api/v1/courier/'
    CREATE_ORDER = '/api/v1/orders'
    GET_ORDER_LIST = '/api/v1/orders'
    CANCEL_ORDER = '/api/v1/orders/cancel'


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {
        'code': 409,
        'message': 'Этот логин уже используется. Попробуйте другой.'
    }
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {
        'code': 400,
        'message': 'Недостаточно данных для создания учетной записи'
    }
    COURIER_ACCOUNT_NOT_FOUND = {
        'code': 404,
        'message': 'Учетная запись не найдена'
    }
    COURIER_LOGIN_NOT_ENOUGH_DATA = {
        'code': 400,
        'message': 'Недостаточно данных для создания учетной записи'
    }


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'


class DataForRegistration:
    reg_data = [
        {'password': generators.generate_password(), 'first_name': generators.generate_firstname()},
        {'login': generators.generate_login(), 'first_name': generators.generate_firstname()}
    ]


class DataForLoginPayloadMissing:
    login_data = [
        {'password': generators.generate_password()},
        {'login': generators.generate_login()}
    ]


class DataForOrder:
    order_payload = {
        'firstName': 'Ivan',
        'lastName': 'Testov',
        'address': 'Razrabotchikov 12',
        'metroStation': 4,
        'phone': '+79991118833',
        'rentTime': 4,
        'deliveryDate': '2025-06-04',
        'comment': 'Draste'
    }
    scooter_color = [
        ['BLACK'],
        ['GREY'],
        (['BLACK'], ['GREY']),
        ['']
    ]
