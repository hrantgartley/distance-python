import inquirer
from requests import get
from simple_chalk import green, blue, yellow

walking_emoji = "🚶"
bus_emoji = "🚌"
plane_emoji = "✈️"

print(blue("Welcome to the travel time calculator!"))

first_city_state = inquirer.prompt(
    [
        inquirer.Text("city", message="Enter the name of the first city"),
        inquirer.Text(
            "state", message="Enter the name of the first state (abbreviated)"
        ),
    ]
)

second_city_state = inquirer.prompt(
    [
        inquirer.Text("city", message="Enter the name of the second city"),
        inquirer.Text(
            "state", message="Enter the name of the second state (abbreviated)"
        ),
    ]
)

# Construct the origin and destination strings for the API request
origin = f"{first_city_state['city']}, {first_city_state['state']}"
destination = f"{second_city_state['city']}, {second_city_state['state']}"

# Make the request to Google Maps Distance Matrix API
api_key = "YOUR_GOOGLE_MAPS_API_KEY"
url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}"
response = get(url)
data = response.json()

# Extract the distance in miles from the API response
distance_miles = (
    data["rows"][0]["elements"][0]["distance"]["value"] * 0.000621371
)  # Convert meters to miles

print(green("\nResults"))
print(blue("-------------------"))
print(
    f"Driving distance between {origin} and {destination}: {distance_miles:.2f} miles"
)
