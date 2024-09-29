import json
import random

import requests

from travello import settings


class SMSService:
    base_url = settings.SMS_API_URL

    @classmethod
    def __get_token(cls):
        data = requests.post(
            url=f'{cls.base_url}auth/login/',
            data={
                'email': settings.SMS_API_EMAIL,
                'password': settings.SMS_API_KEY
            }
        )
        res = data.json()
        return res['data']['token']

    @classmethod
    def send_message(cls, phone_number, message):
        token = cls.__get_token()
        payload = {
            'mobile_phone': phone_number,
            'message': message,
            'from': '4546'
        }
        headers = {
            'Authorization': f'Bearer {token}'
        }
        res = requests.post(
            url=f'{cls.base_url}message/sms/send',
            headers=headers,
            data=payload
        )

    @classmethod
    def get_template(cls):
        token = cls.__get_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        resp = requests.get(
            url=f'{settings.SMS_API_URL}user/templates/',
            headers=headers,
            # data={'template':}
        )


# SMSService.get_template()
# print(requests.get('https://notify.eskiz.uz/api/user/templates'))
# SMSService.get_template()


def generate_code():
    return ''.join(random.sample([f"{i}" for i in range(10)], 4))


def send_message_to_channel(**kwargs):
    keyboard = {
        'inline_keyboard': [
            [
                {
                    'text': 'Завершить',
                    'callback_data': f'answer_yes'
                }
            ],
        ]
    }
    text = f'''
🚫
Имя отправителя: {kwargs['name']}
Почта отправителя: {kwargs['email']}
Сообщение: 
{kwargs['message']}
    '''

    url = settings.TG_API_URL.format(
        token=settings.BOT_TOKEN,
        channel_id=settings.CHANNEL_CHAT_ID,
        text=text
    )
    return requests.post(url, data={'reply_markup': json.dumps(keyboard)})




def send_document_to_channel(**kwargs):
    url = settings.TG_API_URL.format(
        token=settings.SECOND_BOT_TOKEN,
        channel_id=settings.SECOND_CHANNEL_CHAT_ID,
        text=kwargs['msg']
    )
    return requests.post(url)


# test_endpoint = 'http://127.0.0.1:8000/api/v1/main/services/steps/'
# print(requests.get(test_endpoint))

def send_message_for_booking():
    """Sending message of booked event to tg channel."""

