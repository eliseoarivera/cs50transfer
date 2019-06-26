"""def greet(player):
  if player == "Shia":
    return "Welcome, Mr. LeBouf. Nice job on Transformers."
  else:
    return "Welcome, " + player

name1 = input("Enter player 1's name")
print(greet(name1)) # Notice that we're passing a variable as the argument for our greet function.

name2 = input("Enter player 2's name")
print(greet(name2))"""

age = 15

def have_a_birthday():
  global age
  age = 20
  age += 1
  print("Happy birthday! You're now " + str(age))
  return age

have_a_birthday()

print(age)