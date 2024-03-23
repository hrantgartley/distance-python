import inquirer
from geopy import geocoders, distance
from simple_chalk import green, blue, yellow, red

walking_emoji = "🚶"
bus_emoji = "🚌"
plane_emoji = "✈️"
car_emoji = "🚗"

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

# get the latitude and longitude of the first city
try:
    first_location = f"{first_city_state['city']}, {first_city_state['state']}"
    first_geocoder = geocoders.Nominatim(user_agent="distance_calculator")
    first_coords = first_geocoder.geocode(first_location)

    second_location = f"{second_city_state['city']}, {second_city_state['state']}"
    second_geocoder = geocoders.Nominatim(user_agent="distance_calculator")
    second_coords = second_geocoder.geocode(second_location)

    # calculate the distance between the two cities
    walk_distance = distance.distance(
        (first_coords.latitude, first_coords.longitude),
        (second_coords.latitude, second_coords.longitude),
    ).miles
    bus_distance = distance.distance(
        (first_coords.latitude, first_coords.longitude),
        (second_coords.latitude, second_coords.longitude),
    ).miles
    plane_distance = distance.distance(
        (first_coords.latitude, first_coords.longitude),
        (second_coords.latitude, second_coords.longitude),
    ).miles
    car_distance = distance.distance(
        (first_coords.latitude, first_coords.longitude),
        (second_coords.latitude, second_coords.longitude),
    ).miles

    walk_time = walk_distance / 3
    bus_time = walk_distance / 35
    plane_time = walk_distance / 547
    cat_time = walk_distance / 60

    print(green("\nResults"))
    print(blue("-------------------"))
    print(f"Distance between {first_location} and {second_location} by: ")

    print(
        yellow(
            f"{walking_emoji} Walking: {walk_distance:.2f} miles, {walk_time:.2f} hours"
        )
    )
    print(yellow(f"{bus_emoji} Bus: {bus_distance:.2f} miles, {bus_time:.2f} hours"))
    print(
        yellow(
            f"{plane_emoji} Plane: {plane_distance:.2f} miles, {plane_time:.2f} hours"
        )
    )

except TypeError:
    print(red("One of the cities you entered is not valid. Please try again."))

finally:
    print(blue("Goodbye!"))
