class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print('Price: ' + str(self.price))
        print('Speed: ' + str(self.speed))
        print('Fuel: ' + str(self.fuel))
        print('Mileage: ' + str(self.mileage))
        print('Tax: ' + str(self.tax))
car1 = Car(2000, "35mph", "Full", "25mpg")
car2 = Car(20000, "135mph", "Full", "15mpg")
car1.display_all()
car2.display_all()