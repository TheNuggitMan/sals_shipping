print("""
Welcome to Sal's Shipping. 
There are 3 types of shipping:
1: Ground Shipping - flate rate plus price per Kg
2: Ground Shipping Premium - one fee for all weights
3: Drone Shipping - Only weight based.
""")

weight = 124
type_of_shipping = 1

if type_of_shipping == 1: 
  if weight <= 2:
    weight *= 1.50
  elif weight > 2 or weight <= 6:
    weight *= 3
  elif weight > 6 or weight <= 10:
    weight *= 4
  elif weight > 10:
    weight *= 4.75

if type_of_shipping == 3: 
  if weight <= 2:
    weight *= 4.50
  elif weight > 2 or weight <= 6:
    weight *= 9
  elif weight > 6 or weight <= 10:
    weight *= 12
  elif weight > 10:
    weight *= 14.25


if weight == 0 or type_of_shipping == 0:
  print("Please enter valid shipping details")

if type_of_shipping ==1:
  print("You have chosen Ground Shipping. The price is: £" + str(weight + 20))
elif type_of_shipping == 2:
  print("You have chosen Ground Shipping Premium. The price is: £125")
elif type_of_shipping == 3:
  print("You have chosen Drone Shipping. The price is: £" + str(weight))
