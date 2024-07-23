class Restaurant:
    """
    Models aspects of a restaurant
    Name, Cuisine, Status, Clients served
    """

    def __init__(self, res_name, res_cuisine):
        """Initialize the restaurant's attributes"""
        self.res_name = res_name
        self.res_cuisine = res_cuisine
        self.isOpen = False
        self.number_served = 0

    '''Using this method we invert the state of the restaurant using the not operator (review this operator)'''
    def openOrClose(self):
        self.isOpen = not self.isOpen

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

    '''Here we use the ternary operator to print the actual state of the restaurant (open or closed)'''
    def describeRes(self):
        print(f"Restaurant Name: {self.res_name}")
        print(f"Cuisine: {self.res_cuisine}")
        print("Open\n" if self.isOpen else "Closed\n")



res1 = Restaurant("Havana", "Chinese")
res1.openOrClose()
res1.describeRes()

res2 = Restaurant("El Taco", "Mexican")
res2.describeRes()

res3 = Restaurant("Patel", "Hindi")
res3.describeRes()

print(f"Served: {res1.number_served}")
res1.set_number_served(44)
res1.increment_number_served(2)
print(f"Served: {res1.number_served}")

print("\n")
