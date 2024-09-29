from django.conf import settings


def create_event_booked_message(data: dict):
    return f'''
Бронь тура: <b>{data['event']}</b>

Пользователь: <b>{data['user']}</b>
Количество взрослых: <b>{data['total_adult']}</b>
Количество детей: <b>{data['total_children']}</b>
Тип тура: <b>{data['event_type']}</b>
'''


def send_event_booked_message(channel_url: str, data: dict):
    msg = create_event_booked_message(data)
    url = settings.TG_API_URL
