from .Cart import Cart
from.israeli_vat import IsraeliVat
from .tar3_changing_tax import TaxExempt

class Checkout:
    def __init__(self, cart, tax):
        self.cart = cart
        self.tax = tax

    def total(self):
        cart = self.cart.subtotal()
        plus_vat = self.tax.apply(cart)
        return plus_vat
