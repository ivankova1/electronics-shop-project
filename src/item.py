# -*- coding: windows-1251 -*-
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
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
        """Сеттер для имени товара с проверкой длины."""
        if len(value) > 10:
            value = value[:10]  # Обрезаем строку до 10 символов
        self.__name = value

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
    def instantiate_from_csv(cls, file_path) -> None:
        """Класс-метод, инициализирующий экземпляры класса Item данными из файла items.csv."""
        with open(file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)
    @staticmethod
    def string_to_number(s):
        # Преобразуем строку в число с плавающей запятой
        num = float(s)
        # Если дробная часть равна 0, возвращаем целое число
        if num.is_integer():
            return int(num)
        # В противном случае возвращаем целое число, отбрасывая дробную часть
        return int(num)

    def __repr__(self):
        return f"Item({self.__name!r}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"
