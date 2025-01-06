import csv


class InstantiateCSVError(Exception):
    """Исключение, возникающее при ошибках инициализации из CSV файла."""
    pass
class Item:
    """ Класс для представления товара в магазине. """

    pay_rate = 1.0
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:

        self.name = name  # Используем сеттер для установки имени
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # Добавляем текущий экземпляр в список всех товаров



    @property
    def name(self) -> str:
        """Геттер для имени товара."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value
    """Сеттер для имени товара."""


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity * Item.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate


    @classmethod
    def instantiate_from_csv(cls, file_path='items.csv') -> None:
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла items.csv."""
        try:
            with open(file_path, newline='', encoding='UTF-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Проверяем наличие необходимых колонок
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл item.csv поврежден")

                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception as e:
            raise InstantiateCSVError(f"Произошла ошибка: {e}")

    @staticmethod
    def string_to_number(s):
        # Преобразуем строку в число с плавающей запятой
        num = float(s)
        # Если дробная часть равна 0, возвращаем целое число
        if num.is_integer():
            return int(num)
        # В противном случае возвращаем целое число, отбрасывая дробную часть
        return int(num)

    def __add__(self, other):
        if isinstance(other, Item):  # Проверяем, является ли other экземпляром Item
            return self.quantity + other.quantity
        else:
            return NotImplemented  # Возвращаем NotImplemented, если сложение невозможно

    def __repr__(self):
        return f'Item({self.__name!r}, {self.price}, {self.quantity})'

    def __str__(self):
        return f"{self.__name}"
