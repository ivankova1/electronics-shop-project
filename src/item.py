# -*- coding: windows-1251 -*-
import csv
class Item:
    """
    ����� ��� ������������� ������ � ��������.
    """
    pay_rate = 1.0
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:

        self.name = name  # ���������� ������ ��� ��������� �����
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # ��������� ������� ��������� � ������ ���� �������

    @property
    def name(self) -> str:
        """������ ��� ����� ������."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """������ ��� ����� ������ � ��������� �����."""
        if len(value) > 10:
            value = value[:10]  # �������� ������ �� 10 ��������
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        ������������ ����� ��������� ����������� ������ � ��������.
        """
        return self.price * self.quantity * Item.pay_rate

    def apply_discount(self) -> None:
        """
        ��������� ������������� ������ ��� ����������� ������.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path) -> None:
        """�����-�����, ���������������� ���������� ������ Item ������� �� ����� items.csv."""
        with open(file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)
    @staticmethod
    def string_to_number(s):
        # ����������� ������ � ����� � ��������� �������
        num = float(s)
        # ���� ������� ����� ����� 0, ���������� ����� �����
        if num.is_integer():
            return int(num)
        # � ��������� ������ ���������� ����� �����, ���������� ������� �����
        return int(num)

    def __repr__(self):
        return f"Item({self.__name!r}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"
