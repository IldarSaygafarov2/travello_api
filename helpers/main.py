import random
from travello import settings
import requests


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
        print(res.text)

    @classmethod
    def get_template(cs):
        token = cs.__get_token()
        headers = {
            'Authorization': f'Bearer {token}'
        }
        resp = requests.post(
            url=f'{settings.SMS_API_URL}user/template',
            headers=headers
        )
        print(resp.text)


# SMSService.get_template()


def generate_code():
    return ''.join(random.sample([f"{i}" for i in range(10)], 6))
