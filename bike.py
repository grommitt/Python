class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print ('the price of the bike is: ' + str(self.price))
        print ('the miximum speed of the bike is: ' + str(self.max_speed))
        print ('the total miles of the bike is: ' + str(self.miles))
        return self
    def ride(self):
        print ('Riding')
        self.miles += 10
        print ('total miles is now: ' + str(self.miles))
        return self
    def reverse(self):
        print ('Reversing')
        self.miles -= 5
        print ('total miles is now: ' + str(self.miles))
        return self
bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()
"""  Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods?   """
    
