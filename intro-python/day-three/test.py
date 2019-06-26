import basicObjectOrientation

product1 = basicObjectOrientation.Product("Pillow Pal", 24.99)
product1.receive(100)
product1.sell(7)
print(product1.stock)