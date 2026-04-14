def hotel_cost(num_nights):
    """
    Calculate the cost of staying at the hotel
    Parameters: The number of night stayed at the hotel
    Return: The number of days multiplied by the cost
    """
    return num_nights * 560


def plane_cost(city_flight):
    """
    Calculate the cost of the flights
    Parameters: The city you are flying to
    Return: The cost of the flight
    """
    city_name = city_flight.upper()
    if city_name == "DURBAN":
        return 500
    elif city_name == "CAPE TOWN":
        return 800
    elif city_name == "PORT ELIZABETH":
        return 200
    elif city_name == "PRETORIA":
        return 600
    else:
        return -1


def car_rental(rental_days):
    """
    Calculated the cost of the car rental
    Parameters: The number of days a rental is required
    Return: The number of days multiplied by the price per day
    """
    return rental_days * 1000


def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculated the total cost of a holiday
    Parameters: rental_days (the number of days a car rental is required)
                city_flight (where you are flying to)
                num_nights (the number of nights you are staying)
    Return: The car rental cost + plane costs + hotel costs
    """
    if num_nights < rental_days:
        print("A car cannot be rented for more days than the trip")
        exit()

    car_rental_costs = car_rental(rental_days)
    plane_costs = plane_cost(city_flight)
    if plane_costs == -1:
        print("Please enter a valid city")
        exit()
    hotel_costs = hotel_cost(num_nights)
    total = car_rental_costs + plane_costs + hotel_costs
    return total


city_flight = input("Enter the city you will be flying to: ")
num_nights = int(input("Enter the number of nights you will be staying for: "))
rental_days = int(input("Enter the number of days you require a rental car for: "))
total_cost = holiday_cost(num_nights, city_flight, rental_days)
print("\n--- Holiday Cost Breakdown ---")
print(f"Destination: {city_flight}")
print(f"Hotel cost: {hotel_cost(num_nights)}")
print(f"Flight cost: {plane_cost(city_flight)}")
print(f"Car rental cost: {car_rental(rental_days)}")
print(f"Total cost: {total_cost}")
