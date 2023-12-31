# 1.Introduction to Functions
# Functions are a convenient way to group our code into reusable blocks. A function contains a sequence of steps that
# can be performed repeatedly throughout a program without having to repeat the process of writing the same code again.

# 2.Why Functions?

# 3.Defining a Function
# The def keyword indicates the beginning of a function (also known as a function header).

def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")


# 4.Calling a Function
# To call our function, we must type out the function’s name followed by a pair of parentheses and no indentation:
directions_to_timesSq()


def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station.")
    print("Take the Northbound N, Q, R, or W train 1 stop.")
    print("Get off the Times Square 42nd Street stop.")
    print("Take lots of pictures!")


directions_to_timesSq()

# 5.Whitespace & Execution Flow
print("Checking the weather for you!")


def weather_check():
    print("Looks great outside! Enjoy your trip.")


print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")
weather_check()


# 6.Parameters & Arguments
# The parameter is the name defined in the parenthesis of the function and can be used in the function body.
def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


generate_trip_instructions("Central Park")

generate_trip_instructions("Grand Central Station")


# 7.Multiple Parameters
# We can write a function that takes in more than one parameter by using commas:

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    trip_total = car_rental_total + hotel_total + plane_ticket_price
    print(f"trip_total is {trip_total}")
    return trip_total


calculate_expenses(200, 100, 100, 5)


# 8.Types of Arguments
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print(f"First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")


trip_planner("France", "Germany", "Denmark")

trip_planner("Denmark", "France", "Germany")

trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

trip_planner("Brooklyn", "Queens")

# 9.Built-in Functions vs User Defined Functions

help("string")

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00


# Write your code below:
def max_price():
    max_price = max(9.75, 15.50, 5.99, 2.00)
    print(max_price)


max_price()

min_price = min(9.75, 15.50, 5.99, 2.00)
print(min_price)

rounded_price = round(tshirt_price, 1)
print(rounded_price)


# 10.Variable Access
# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
    favorite_locations = "Paris, Norway, Iceland"
    print("There are 3 locations")


# This function will print the favorite locations
def show_favorite_locations(favorite_locations):
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations("Paris, Norway, Iceland")

# 11.Returns
# Functions can also return a value to the program so that this value can be modified or used later.
# We use the Python keyword return to do this.
current_budget = 3500.75


def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))


print_remaining_budget(current_budget)

# Write your code below:
shirt_expense = 9


def deduct_expense(budget, expense):
    return budget - expense


new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


# 12.Multiple Returns
def top_tourist_locations_italy():
    first = "Rome"
    second = "Venice"
    third = "Florence"
    return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)


# 13.Review
def trip_planner_welcome(name):
    print(f"Welcome to tripplanner v1.0 {name} ")


trip_planner_welcome("Steven")


def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


estimate = estimated_time_rounded(50.55)


def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print(f"Your trip starts off in {origin} ")
    print(f"And you are traveling to {destination} ")
    print(f"You will be traveling by {mode_of_transport}")
    print(f"It will take approximately {estimated_time} hours")


destination_setup("China", "London", estimate)
