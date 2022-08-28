import requests


class Covalent:
    def __init__(self, chain_id=137):
        self.api_key = 'ckey_09cd45e4ba81458ebe96052a603'
        self.base_url = 'https://api.covalenthq.com/v1/'
        self.session = requests.session()
        self.chain_id = chain_id

    def get_token_price_details(self, address, start_date, end_date=None):
        """date_format: YYYY-MM-DD"""
        end_date = end_date or start_date
        endpoint = f'pricing/historical_by_addresses_v2/{self.chain_id}/USD/{address}/?quote-currency=USD&format=JSON&from={start_date}&to={end_date}&key={self.api_key}'
        url = self.base_url + endpoint
        result = self.session.get(url).json()
        data = result["data"]
        # print(data)
        return data

    def get_token_price_and_decimal_at_date(self, address, price_date):
        result = self.get_token_price_details(address, price_date)
        price = result[0]['prices'][0]['price']
        decimal = result[0]['contract_decimals']
        return price, decimal


def main():
    result = Covalent().get_token_price_details("0x0b3f868e0be5597d5db7feb59e1cadbb0fdda50a", "2022-08-26", "2022-08-26")
    breakpoint()


if __name__ == '__main__':
    main()
