import requests

def get_flight_prices(origin, destination, date):
    # Flight API request (use real API key)
    api_key = 'your_amadeus_api_key'
    url = f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={destination}&departureDate={date}&adults=1'
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def get_facebook_events(city, date, access_token):
    # Facebook API request (use real access token)
    url = f"https://graph.facebook.com/v12.0/search?type=event&q={city}&since={date}&access_token={access_token}"
    response = requests.get(url)
    return response.json()['data'] if response.status_code == 200 else None

def get_weather(city, date):
    # Weather API request (use real API key)
    api_key = "your_openweather_api_key"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&date={date}&appid={api_key}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None
