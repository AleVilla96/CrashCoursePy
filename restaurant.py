class Restaurant:
    def __init__(self, res_name, res_cuisine):
        self.res_name = res_name
        self.res_cuisine = res_cuisine
        self.isOpen = False

    '''Using this method we invert the state of the restaurant using the not operator (review this operator)'''
    def openOrClose(self):
        self.isOpen = not self.isOpen

    '''Here we use the ternary operator to print the actual state of the restaurant'''
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
