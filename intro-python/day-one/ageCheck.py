age = input("How old are you?")

"""if age >= "18":
  print("You're old enough to vote!")
else:
  print("You're not old enough to vote.")"""
  
age = input("How old are you?") # Read this as "Set age equal to whatever string the user types."
age = int(age) # We reassign the variable information here.
# In essence, "Set age equal to an integer expression of whatever the user typed."

if age >= 18:
  print("You're old enough to vote!")
else:
  print("You're not old enough to vote.")