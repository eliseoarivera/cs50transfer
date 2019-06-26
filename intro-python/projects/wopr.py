print("Welcome benders, please login to the avatar.net...")

def greeting(name, bender, loc):
  if name.lower() == "aang" and (bender.lower() == "all" or bender.lower() == "all elements") and (loc.lower() == "air temple" or loc.lower() == "air nomad"):
    password = input("What is your password?")
    if password == "yip yip":
      return "OMG You are the Avatar! Welcome."
    elif password == "exit":
      return "Shutting Down"
    else:
      print ("Wrong Password")
      return greeting(name, bender, loc)
  elif name.lower() == "katara" and bender.lower() == "water" and loc.lower() == "Southern Water Tribe":
    return "Welcome, Katara."
  elif name.lower() == "appa":
    return "Hey Appa!"
  else:
    return ("Greetings, " + name + ", " + bender + "bending citizen of " + loc + "!")
    
name = input("What is your name?")
bender = input("What element do you bend?")
loc = input("What location are you from?")

print(greeting(name, bender, loc))
