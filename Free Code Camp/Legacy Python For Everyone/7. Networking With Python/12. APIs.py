import requests

# Replace 'your_api_key_here' with your actual CoinMarketCap API key
api_key = '9b935560-b70c-4612-8ae6-63251d62e4a4'

# Define the API endpoint and parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'
parameters = {
    'start': '1',
    'limit': '100',  # Number of cryptocurrencies to fetch
    'convert': 'USD'
}

# Set up the headers with your API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

try:
    # Make the request to the CoinMarketCap API
    response = requests.get(url, headers=headers, params=parameters)

    # Check if the request was successful
    response.raise_for_status()  # Will raise an HTTPError for bad responses

    # Parse the response JSON
    data = response.json()
    crypto_list = list()
    # Print the response or process it as needed
    for crypto in data['data']:
        market_cap = crypto['quote']['USD']["market_cap"]
        if market_cap < 50000000000000:
            name = crypto['name']
            symbol = crypto['symbol']
            price = crypto['quote']['USD']['price']
            crypto_list.append((market_cap, name, symbol, price))
            #print(f"{name} ({symbol}): ${price:.2f}, MarketCap: ${market_cap:.2f}")
    crypto_list.sort(reverse=True)
    crypto_list = crypto_list[0:10]
    for i in crypto_list:
        print(format(i[1],"20.20s"),":", format(i[0],"16.2f"))
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
