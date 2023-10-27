class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product: str):
        self.products.append(product)

    def get_by_letter(self, letter: str):
        return [product for product in self.products if product.startswith(letter)]

    def __repr__(self):
        string_to_return = f"Items in the {self.name} catalogue:\n"
        string_to_return += "\n".join(sorted(self.products))
        return string_to_return

