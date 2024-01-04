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
