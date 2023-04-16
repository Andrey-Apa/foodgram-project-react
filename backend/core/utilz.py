from datetime import datetime as dt
import pytz
import requests


def get_user_time(request):
    """Получение времени пользователя из запроса.
    >> Определяем IP пользователя из заголовка запроса
    >> Получаем временную зону через API сервиса ip-api.com
    >> Получаем текущее время пользователя в его зоне.
    В случае неверной зоны или ее отсутсвия используется время по UTC.
    """
    user_ip = request.META.get('HTTP_X_REAL_IP')
    if user_ip is None:
        return dt.now(pytz.utc)
    try:
        response = requests.get(
            url=f'http://ip-api.com/json/{user_ip}').json()
    except requests.exceptions.ConnectionError:
        print('Нет соединения с сервисом ip-api!')
    user_timezone = response.get('timezone')
    try:
        tzinfo = pytz.timezone(user_timezone)
        return dt.now(tz=tzinfo)
    except pytz.exceptions.UnknownTimeZoneError:
        return dt.now(pytz.utc)
