from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ConvertedPricePLN:
    price_in_source_currency: float
    currency: str
    currency_rate: float
    currency_rate_fetch_date: str
    price_in_pln: float


class PriceCurrencyConverterToPLN:
    @staticmethod
    def convert_to_pln(*, currency: str, price: float, currency_rate: float) -> ConvertedPricePLN:
        return ConvertedPricePLN(price, currency, currency_rate, datetime.today().strftime('%Y-%m-%d'), round(price * currency_rate, 2))
