class IsraeliVat:
    VAT = 0.17
    def apply(self, amount):
        vat_itself = amount * IsraeliVat.VAT
        return amount + vat_itself
