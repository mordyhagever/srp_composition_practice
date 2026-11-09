from classes.checkout import *
from classes.tar3_changing_tax import TaxExempt
cart = Cart()
cart.add("Pen", 5, 4)
cart.add("Bag", 60)
checkout_with_tax = Checkout(cart, IsraeliVat())
checkout_without_tax = Checkout(cart, TaxExempt())
print(checkout_with_tax.total())
print(checkout_without_tax.total())