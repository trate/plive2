# plive2.py: classes and methods
class Price:
    def __init__(self, part_number, price):
        self.price = price
        self.part_number = part_number

    def get_price(self):
        return self.price

my_object = Price(2, 10)
print(my_object.get_price())

def function__init__(self, part_number, price):
    self.price = price
    self.part_number = part_number


def function_get_price(self):
    return self.price

namespace = {'__init__': function__init__, 'get_price': function_get_price}

Price2 = type('Price2', (), namespace)
my_object2 = Price2(2, 11)
print(my_object2.get_price())