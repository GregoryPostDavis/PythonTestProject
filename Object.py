class Object:

    quantity = 1

    def __init__(self, name = "Item"):
        if name:
            self.name = name

    def print_value(self):
        print("Value: ", self.name)

    def set_quantity(self, quantity):
        self.quantity = quantity
