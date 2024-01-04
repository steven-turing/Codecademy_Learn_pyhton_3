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
  max_price = max(9.75,15.50,5.99,2.00)
  print(max_price)

max_price()

min_price = min(9.75,15.50,5.99,2.00)
print(min_price)

rounded_price = round(tshirt_price,1)
print(rounded_price)