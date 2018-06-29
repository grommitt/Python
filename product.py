class Product:
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price += self.price * tax
        return self

    def returns(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if reason_for_return == "like_new":
            self.status = "for sale"
            return self
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price*.8
            return self
        

    def displayInfo(self):
        print("--------------------------------------")
        print("Price: " + str(self.price))
        print("Item Name: " + str(self.name))
        print("Weight: " + str(self.weight))
        print("Brand: " + str(self.brand))
        print("Cost: " + str(self.cost))
        print("Status: " + str(self.status))
        print("--------------------------------------")

shirt = Product(20, "T-Shirt", "1.1kg", "Hurley", 5)
shirt.add_tax(.15).sell().displayInfo()
shirt.add_tax(.15).sell().returns("defective").displayInfo()
surfboard = Product(200, "Longboard", "35pounds", "Curve", 100)
surfboard2 = Product(200, "Longboard", "35pounds", "Curve", 100)
surfboard.add_tax(.15).sell().displayInfo()
surfboard2.displayInfo()
    


        