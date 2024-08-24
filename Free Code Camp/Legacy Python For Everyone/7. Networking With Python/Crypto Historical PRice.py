import requests
import datetime

# Replace with your actual CoinMarketCap API key
api_key = '9b935560-b70c-4612-8ae6-63251d62e4a4'

# Define the API endpoint for historical data
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'

# Set the parameters for the request
parameters = {
    'symbol': 'BTC',
    'convert': 'USD',
    'time_start': '2024-01-01',  # Start date in YYYY-MM-DD format
    'time_end': '2024-01-31'  # End date in YYYY-MM-DD format
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
    response.raise_for_status()

    # Parse the response JSON
    data = response.json()

    # Print or process the historical price data
    for quote in data['data']['quotes']:
        timestamp = quote['timestamp']
        price = quote['quote']['USD']['price']
        date = datetime.datetime.fromisoformat(timestamp).strftime('%Y-%m-%d')
        print(f"Date: {date}, Price: ${price:.2f}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
