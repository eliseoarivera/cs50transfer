name = "Lauren"
name2 = "Eliseo"

print("Good morning " + name + "!")
print("Good morning %s!" % name2)

name = "Eliseo"
age = "28"

print("Good morning " + name + "!")
print(name + " is " + age + " years old! ")

"""name = input("What is your name?")

if name == "Beyonce":
  print("Welcome, queen B.")
else:
  print("Greetings, " + name + "! Welcome to the program.")"""
  
name = input("What is your name?")
password = input("Please enter your password.")

if name == "Beyonce" and password == "Lemonade1":
  print("Welcome, queen B.")
elif password != "Lemonade1":
  print("WARNING. Incorrect password")
else:
  print("Greetings, " + name + "! Welcome to the program.")

