# Define the class
"""class Product:
  # Define the __init__ method
  def __init__(self, this_product_name, this_product_price):
    print(this_product_name + " created successfully!")

class Product:
  # Define the initialize method
  def __init__(self, this_product_name, this_product_price, this_product_stock):
    self.name = this_product_name 
    self.price = this_product_price
    self.stock = this_product_stock
    print(self.name + " created successfully!\n The price is " + str(self.price) + " with " + str(self.stock) + " left in stock.")

# Initialize the first product
product1 = Product("Pillow Pal", 24.99, 10)
product2 = Product("Pokeball", 4.00, 25)
product3 = Product("Sandwich", 6.00, 3)
Product4 = Product("Kitty", 120.00, 2)
Product5 = Product("Keyblade", 1000.00, 1)"""
#print(id(product1)) #code to prove its all working

# Define the class

# Initialize the first product

#custom methods
#Define the class.
class Product:

  # Define the initialize method.
  def __init__(self, this_product_name, this_product_price):
    self.name = this_product_name #method
    self.price = this_product_price #method
    self.stock = 0 
    print(self.name + " created successfully!")

  def receive(self, quantity):#quantity is a number
    self.stock += quantity # receiving 100

  def sell(self, quantity):
    self.stock -= quantity#selling 7
  

class Cart:
  def __init__(self, discount = 0.0):
    self.items = []
    self.discount = discount
    self.total = 0
    print("New cart created!")

  def compute_total(self):
    self.total = 0
    for product in self.items:
      self.total += product.price
    return self.total

  def add_item(self, product, quantity = 1):
    if product.stock == 0:
      print("Sorry, we're out of " + product.name + " at the moment.")
      return False
    elif product.stock < quantity:
      print("Sorry, we only have " + str(product.stock) + " " + product.name + "(s) on hand. Please reduce the quantity and try again.")
      return False
    else:
      for _ in range(quantity):
        self.items.append(product)
      print("Item(s) added successfully!")
      self.compute_total()
      print("Your new total is " + str(self.total) + ".")
      
# Initialize the first product
product1 = Product("Pillow Pal", 24.99)
# Receive 100 pillow pals
product1.receive(13)
# Sell 7
product1.sell(10)
# Confirm that we have 93 left
#print(product1.stock)

mycart = Cart()
mycart.add_item(product1, 3)
#print(mycart.total)


#play with this later
"""class CustomerAccount:
  def __init__(self, name):
    self.name = name
    print(self.name + " created successfully!")

customer1 = CustomerAccount("Eli")"""