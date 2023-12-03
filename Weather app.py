
import json

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "http://api.openweathermap.org/data/2.5/forecast"
        self.favorite_locations = {}

    def get_weather_data(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # You can change units to imperial for Fahrenheit
        }
        response = requests.get(self.base_url, params=params)
        return response.json() if response.status_code == 200 else None

    def get_forecast_data(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.forecast_url, params=params)
        return response.json() if response.status_code == 200 else None

    def display_weather(self, weather_data):
        if weather_data:
            print("\nCurrent Weather:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
            print(f"Weather Condition: {weather_data['weather'][0]['description']}")
        else:
            print("Error fetching weather data. Please check the city name and try again.")

    def display_forecast(self, forecast_data):
        if forecast_data:
            print("\nWeather Forecast for the next few days:")
            for forecast in forecast_data['list']:
                print(f"{forecast['dt_txt']}: {forecast['main']['temp']}°C, {forecast['weather'][0]['description']}")
        else:
            print("Error fetching forecast data. Please check the city name and try again.")

    def save_favorite_location(self, city):
        self.favorite_locations[city] = True
        print(f"{city} added to favorites.")

    def view_favorite_locations(self):
        if self.favorite_locations:
            print("\nFavorite Locations:")
            for city in self.favorite_locations:
                print(city)
        else:
            print("No favorite locations yet.")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    weather_app = WeatherApp(api_key)

    while True:
        print("\nWeather App Menu:")
        print("1. Get Current Weather")
        print("2. Get Weather Forecast")
        print("3. Save Favorite Location")
        print("4. View Favorite Locations")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            city = input("26 degree celsius: ")
            weather_data = weather_app.get_weather_data(city)
            weather_app.display_weather(weather_data)
        elif choice == '2':
            city = input("Enter the city name: ")
            forecast_data = weather_app.get_forecast_data(city)
            weather_app.display_forecast(forecast_data)
        elif choice == '3':
            city = input("Enter the city name to save as a favorite: ")
            weather_app.save_favorite_location(city)
        elif choice == '4':
            weather_app.view_favorite_locations()
        elif choice == '5':
            print("Exiting the Weather App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
