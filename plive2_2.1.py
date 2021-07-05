# plive2_2.1.py: dir and __dict__
class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return self.price

item_price = Price("AAAA_BBB", 10)

print("Explore instance with a dir function")
print(dir(item_price))

print("Explore class with a dir function")
print(dir(Price))

print("Explore instance with a __dict__ attribute")
print(item_price.__dict__)

print("Explore class with a __dict__ attribute")
print(Price.__dict__)

def set_discount(self, percent_off):
   self.percent_off = percent_off

def get_discount(self):
    return self.price * (self.percent_off/100)

Price.set_discount = set_discount
Price.get_discount = get_discount

item_price2 = Price("LLL-VBF", 20)
print(item_price2.__dict__)
print(dir(item_price2))
