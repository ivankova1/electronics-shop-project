from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)  # Вызываем конструктор родительского класса
        self.number_of_sim = number_of_sim  # Количество поддерживаемых SIM-карт

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value


    def __add__(self, other):
        if isinstance(other, Item):  # Проверяем, является ли other экземпляром Item
            return self.quantity + other.quantity
        elif isinstance(other, Phone):  # Проверяем, является ли other экземпляром Phone
            return self.quantity + other.quantity
        else:
            return NotImplemented  # Возвращаем NotImplemented, если сложение невозможно


    def __repr__(self):
        return f"Phone({self.name!r}, {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

