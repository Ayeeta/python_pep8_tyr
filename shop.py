'''Shopping Cart class has methods to add, remove items from shopping
   cart and also check balance

'''


class ShoppingCart(object):
    '''class contains methods to add, remove from cart and check bal'''

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        '''Adds item to the shopping cart'''
        if quantity > 0 and price > 0:
            cost = price * quantity
            self.total += cost
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        '''Removes items from the shopping cart'''

        if item_name in self.items:
            cost = quantity * price
            if quantity < self.items[item_name]:
                self.total -= cost
                self.items[item_name] = self.items[item_name] - quantity
            elif quantity == self.items[item_name]:
                del self.items[item_name]
                self.total -= cost
            elif quantity > self.items[item_name]:
                real_cost = self.items[item_name] * price
                del self.items[item_name]
                self.total -= real_cost

    def checkout(self, cash_paid):
        '''method to check available balance'''

        if isinstance(cash_paid, int):
            balance = 0
            if cash_paid > self.total:
                balance = cash_paid - self.total
                return balance
            else:
                return "Cash paid not enough"
        else:
            raise TypeError("Check your values entered")


class Shop(ShoppingCart):
    '''this class reduces items from the shop'''

    def __init__(self):
        ShoppingCart.__init__(self)
        self.quantity = 100


    def remove_item(self, item_name=False, quantity=False, price=False):
        '''method reduces quantity of an item in the shop'''
        self.quantity -= 1
