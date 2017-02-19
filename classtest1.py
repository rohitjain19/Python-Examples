class test(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price



banana = test("banana", 12)
#print ("This is banana", banana)
print (banana.make,banana.price)


banana.price = 15
print(banana.price)

orange = test("orange",6)
print("models: {} = {} , {} = {}".format(banana.make,banana.price,orange.make,orange.price))

print ("models: {0.make} = {0.price},{1.make}={1.price}".format(banana,orange))