#Sal's Shipping

weight = 41.5

#Ground Shipping
if  weight <= 2:
   cost_ground = weight * 1.5 + 20
elif weight <=6:
  cost_ground = weight * 3 + 20
elif weight <=10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground Shipping :$",cost_ground)

cost_premium = 125
#print(cost_premium)
print("Ground Shipping premium:$", cost_premium  )

#Drone Shipping
if  weight <= 2:
   cost_drone = weight * 4.5
elif weight <=6:
  cost_drone = weight * 9
elif weight <=10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25
print("Ground Shipping drone:$",cost_drone)