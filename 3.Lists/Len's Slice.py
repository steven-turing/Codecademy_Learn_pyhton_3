# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print("We sell [" + str(num_pizzas) + "] different kinds of pizza!")

# zip()
pizza_and_prices = [[price, topping] for (price, topping) in zip(prices, toppings)]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

pizza_and_prices.pop()

pizza_and_prices.append([2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

# The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs.
# Each pair contains one element from each of the inputs.

# This zip object contains the location of this variable in our computer’s memory. Don’t worry though,
# it is fairly simple to convert this object into a useable list by using the built-in function list():
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)