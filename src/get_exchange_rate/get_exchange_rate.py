from abc import ABC, abstractmethod
from src.connectors.local import LocalJsonLoader
from datetime import datetime
import requests


class ExchangeRate(ABC):
    def __init__(self, url: str, curr):
        self.url = url
        self.curr = curr

    @abstractmethod
    def load_rate(self):
        pass


class LocalExchangeRate(ExchangeRate):
    def __init__(self, url: str, curr: str):
        super().__init__(url, curr)

    def load_rate(self):
        return self.load_rate_from_local_file()

    def load_rate_from_local_file(self):
        loader = LocalJsonLoader(self.url)
        loader = loader.get_local_file_data()
        self.curr_rate = -1
        if self.curr.upper() not in loader.keys():
            return 0
        for d in loader[self.curr.upper()]:
            if d["date"] == datetime.today().strftime('%Y-%m-%d'):
                self.curr_rate = d["rate"]
                break
        return self.curr_rate


class APIExchangeRate(ExchangeRate):
    def __init__(self, url: str, curr: str):
        super().__init__(url, curr)

    def load_rate(self):
        return self.load_rate_from_api()
    
    def load_rate_from_api(self):
        ftc = FetchCurrencyFromAPI('http://api.nbp.pl/api/exchangerates/rates/A')
        self.curr_rate = ftc.fetch_currency(self.curr)
        return self.curr_rate
    

class Rate:
    def __init__(self):
        pass

    def get_rate(self, storage: ExchangeRate):
        return storage.load_rate()
        

class FetchCurrencyFromAPI:
    def __init__(self, url):
        self.api_url = url

    def fetch_currency(self, currency):
        response = requests.get(f'{self.api_url}/{currency}/?format=json')
        if response.status_code == 404:
            return 0
        result = response.json()
        return result['rates'][0]['mid']
