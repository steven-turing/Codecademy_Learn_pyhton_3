# At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great!
# We have four different menus: brunch, early-bird, dinner, and kids.
# Making the Menus
# Create a Menu class .Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        end_time_formatted = self.end_time
        if self.end_time > 12:
            end_time_formatted = self.end_time - 12
            end_period = "pm"
        else:
            end_period = "am"
        return "{name} menu available from {start_time}am to {end_time}{end_period}".format(name=self.name,
                                                                                            start_time=self.start_time,
                                                                                            end_time=end_time_formatted,
                                                                                            end_period=end_period)

    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            price = self.items[item]
            total_price += price
        print(total_price)

    # Let’s create our  menu


brunch = Menu("brunch",
              {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
               'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00, }, 15, 18)

dinner = Menu("dinner",
              {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00,
               'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00, }, 15, 22)

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

print(brunch)
brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])


# Creating the Franchises
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Franchise located at {address}".format(address=self.address)

    def available_menus(self, time):
        available_menus  = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available_menus .append(menu)
        return available_menus


# Let’s create our first two franchises!
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

available_menus_at_noon = flagship_store.available_menus(12)
print(available_menus_at_noon)

available_menus_at_noon1 = flagship_store.available_menus(5pm)
print(available_menus_at_noon1)

# Creating Businesses!
class Business:
  pass 