import random

import http.client
import json

API_URL = '/sms/3/messages'
API_HOST = "8gwv4d.api.infobip.com"
API_KEY = '45f8515bc8e0c47479c742afbaad4514-decc5867-5c17-4d44-80f3-796b4a690475'


def send_sms_code(text, phone_number):
    phone_number = phone_number.replace('+', '')
    conn = http.client.HTTPSConnection(API_HOST)
    payload = json.dumps({
        "messages": [
            {
                "sender": "579",
                "destinations": [
                    {
                        "to": phone_number
                    }
                ],
                "content": {
                    "text": text
                }
            }
        ]
    })
    headers = {
        'Authorization': f'App {API_KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request("POST", API_URL, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def generate_code():
    return ''.join(random.sample([f"{i}" for i in range(10)], 6))
