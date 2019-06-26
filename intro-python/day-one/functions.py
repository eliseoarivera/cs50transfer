"""def shout(name):
  name = name.upper()
  return "HELLO " + name + "!"
print(shout("Britney"))"""

"""def costForDisney(adults, children, days):
  adult_cost = adults * 100
  print("Calculated adult cost at " + str(adult_cost))
  child_cost = children * 90
  print("Calculated child cost at " + str(child_cost))
  daily_cost = adult_cost + child_cost
  total_cost = daily_cost * days
  return total_cost
  
print(costForDisney(3,5,10))"""

"""def num_of_letters(name):
  name = len(name)
  return name
print(num_of_letters("Sandwich"))"""
#Write a function that takes in three numbers and returns the product of all three

"""def productOf(num1, num2, num3):
  total_cost = num1 * num2 * num3
  return total_cost
  
print(productOf(4,5,6))"""
  
#Write a function that takes in a user's name and then returns their name"""

"""def userName(name):
  name = input("What is your name?")
  return "Hello " + name + "!"
print(userName("name"))"""

# Define the function!
"""def personalized_age_check(name, age):
  if age >= 18:
    return "Congratulations " + name + "! You're old enough to vote."
  else:
    time_left = 18 - age
    return "Sorry, " + name + ". You can't vote for another " + str(time_left) + " years."

# Call the function
print(personalized_age_check("Jeff", 28))
print(personalized_age_check("Zara", 14))"""

"""def add(x, y):
  total = x + y
  return total

# Call
print(add(5, 22))"""

# Defenition
def add(x, y):
  print("Adding your numbers")
  total = x + y
  return str(total) + "\nFinished adding."

# Call
print(add(5, 22))