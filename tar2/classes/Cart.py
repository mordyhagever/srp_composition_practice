
class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, quantity=1):
        new_item = {"name": name, "price": price, "quantity": quantity}
        self.items.append(new_item)

    def subtotal(self):
        sum_price = 0
        if not self.items:
            return "Cart is empty"
        for item in self.items:
            sum_price += item["price"] * item["quantity"]
        return sum_price

# new_cart = Cart()
# new_cart.add("rise", 10, 2)
# new_cart.add("chips", 5, 3)
# print(new_cart.subtotal())
# print(new_cart.items)
