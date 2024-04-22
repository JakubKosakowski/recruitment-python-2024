from logging import getLogger
import sys
from src.currency_converter import *
from src.get_exchange_rate import *
from src.save_data import *


logger = getLogger(__name__)
try:

    if len(sys.argv) != 2:
        print("Usage: python myscript.py [dev/prod]")
        exit()
        
    mode = sys.argv[1]

    if mode not in ['dev', 'prod']:
        raise Exception

    print("Welcome to Currency Exchange App\n")
    while True:
        data = input("""Which type of exchange data do you prefer: local or API? """)
        if data.lower().strip() in ['api', 'local']: 
            break
        else:
            print("Wrong exchange data type. Try again")

    while True:
        tmp = input("Enter(currency_code|price_in_source): ")
        if '|' in tmp:
            curr, price = tmp.split('|')
            price = float(price)
            ftc = Rate()
            if data == 'api':
                storage = APIExchangeRate('http://api.nbp.pl/api/exchangerates/rates/A', curr)
            elif data == 'local':
                storage = LocalExchangeRate('./static/example_currency_rates.json', curr)
            
            curr_rate = ftc.get_rate(storage)
            if curr_rate == 0:
                print("There is no currency with this code, try again")
            elif curr_rate == -1:
                print("Sorry, but there is no actual rate for this currency. Try again later.")
                exit()
            else: break
        else:
            print("Wrong input data notation, try again.")
        
    exchange_data = PriceCurrencyConverterToPLN().convert_to_pln(currency=curr, price=price, currency_rate=curr_rate)
    save = SaveData()
    if mode == "dev":
        save_method = SaveToJson('./static/database.json', (exchange_data.currency.lower(), exchange_data.currency_rate, exchange_data.price_in_pln))   
    elif mode == "prod":
        save_method = SaveToDatabase('sqlite:///static/mydb.db',
                                        (exchange_data.currency.lower(),
                                         exchange_data.currency_rate, exchange_data.price_in_pln))
        
    save.save_data(save_method)
    
    print("Successfully exchange! "\
          f"You'll receive {exchange_data.price_in_pln}PLN "\
          f"for your {exchange_data.price_in_source_currency}{exchange_data.currency.upper()}")
    logger.info("Job done!")
except Exception as err:
    print("Sorry, there is no this type of runmode. Only: dev, prod")
