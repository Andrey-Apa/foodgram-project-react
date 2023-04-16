from datetime import datetime as dt
import pytz
import requests


def get_user_time(request):
    """Получение времени пользователя из запроса.
    Определяем IP пользователя, далее временную зону, получаем время.
    """
    user_ip = request.META.get('REMOTE_ADDR')
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
        user_time = dt.now(pytz.utc)
    return user_time
