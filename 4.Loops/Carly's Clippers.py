hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price
print(total_price)

# Try modifying your code to use f-string syntax for the print statement, like this:
average_price = total_price / len(prices)
print(f"The average_price is :{average_price}")

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f"The total_revenue is :{total_revenue}")

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# First, you need to include the index i in your loop, so you can access the corresponding hairstyle in hairstyles.
# Second, you need to append the hairstyles[i] to the cuts_under_30 list, if the new_prices[i] is less than 30.

cuts_under_30 = []
i = 0
for i in range(len(new_prices)):
    if new_prices[i] < 30:
        cuts_under_30.append(hairstyles[i])
print(cuts_under_30)
