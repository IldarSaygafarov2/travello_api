import freecurrencyapi

from travello import settings


class CurrencyService:
    def __init__(self):
        self.client = freecurrencyapi.Client(settings.CURRENCY_API_KEY)

    def get_data(self):
        return self.client.latest(currencies=['RUB'])['data']['RUB']


service = CurrencyService()

