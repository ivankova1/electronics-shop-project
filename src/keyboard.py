from src.item import Item
from src.language_mixin import LanguageMixin


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)  # Инициализируем миксин

    def __repr__(self):
        return f"Keyboard({self.name!r}, {self.price}, {self.quantity}, {self.language!r})"

    def __str__(self):
        return f'{self.name}'

