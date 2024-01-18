# 1.Introduction to Functions
# Functions are a convenient way to group our code into reusable blocks. A function contains a sequence of steps that
# can be performed repeatedly throughout a program without having to repeat the process of writing the same code again.

# 2.Why Functions?
# If our program now had 100 new people trying to find the best directions，
# we would need to run 100 times!Now, if you’re thinking about using a loop here, your intuition would be totally right!
# Unfortunately, we won’t be always traveling between the same two locations which means a loop won’t be as effective
# when we want to customize a trip. We will address this in the upcoming sections!

#For now, let’s gain an appreciation for functions.
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
# In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that
# function.
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

# 9.Built-in Functions vs User Defined Functions There are two distinct categories for functions in the world of
# Python. What we have been writing so far in our exercises are called User Defined Functions - functions that are
# written by users (like us!). help("string")

# There is another category called Built-in functions - functions that come built into Python for us to use. Remember
# when we were using print or str? Both of these functions are built into the language for us, which means we have
# been using built-in functions all along!

# There are lots of different built-in functions that we can use in our programs. Take a look at this example of using
# len() to get the length of a string:

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# There are even more obscure ones like help() where Python will print a link to documentation for us and provide some
# details:
#help("string")
# Would output (shortened for readability):

# Let’s practice using a few of them. You will need to rely on the provided Python documentation links to find your
# answers!
# We were provided a list of prices for some gift shop items:
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Create a variable called max_price and call the built-in function max() with the variables of prices to get the
# maximum price.
def max_price():
    max_price = max(9.75, 15.50, 5.99, 2.00)
    print(max_price)


max_price()

# Using the same set of prices, create a new variable called min_price and use the built-in function min() with the
# variables of prices to get the minimum price.
min_price = min(9.75, 15.50, 5.99, 2.00)
print(min_price)


# Use the built-in function round() to round the price of the variable tshirt_price by one decimal place.
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
# Sometimes we may want to return more than one value from a function. We can return several values by separating them
# with a comma.
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
