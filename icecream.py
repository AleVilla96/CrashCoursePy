#9.6

from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, res_name, res_cuisine):
        super().__init__(res_name, res_cuisine)
        self.flavors = ["Vanilla", "Chocolate", "Mascarpone"]

    def show_flavors(self):
        print("Flavors: ")
        for item in self.flavors:
            print(item)


ice_stand1 = IceCreamStand("Helado Oscuro de la Luna", "Helados")

ice_stand1.describeRes()
ice_stand1.show_flavors()