def welcome_message():
    print('Welcome to the Weather App!')

def ask_for_city():
    return input('What city would you like the weather for: ')

def get_weather_data():
    return {
        "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"},
        "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"},
        "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"},
        "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"},
        "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"}
    }

def fetch_data(city, weather_data):
    return weather_data.get(city, None)

def display_data(city, weather):
    print(f'Weather for {city}:')
    print(f'Current temperature: {weather["temperature"]}')
    print(f"Weather conditions: {weather['conditions']}")
    print(f"Wind speed: {weather['wind_speed']}")
    print(f"Humidity: {weather['humidity']}")

def thank_you_message():
    print('Thank you for using the Weather App!')

def main():
    welcome_message()
    weather_data = get_weather_data()

    while True:
        city = ask_for_city()
        weather = fetch_data(city, weather_data)
        
        if weather:
            display_data(city, weather)
            break
        else:
            print(f'Sorry, we do not have any data for {city}. Please try again.')

    thank_you_message()

if __name__ == "__main__":
    main()
