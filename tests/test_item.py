"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture(autouse=True)
def clear_item_list():
    # Очищаем список всех экземпляров перед каждым тестом
    Item.all.clear()
    Item.pay_rate = 1.0  # Сбрасываем pay_rate перед каждым тестом


def test_item_creation():
    item = Item("Смартфон", 10_000, 20)
    assert item.name == "Смартфон"
    assert item.price == 10_000
    assert item.quantity == 20
    assert len(Item.all) == 1

def test_calculate_total_price_without_discount():
    item = Item("Ноутбук", 20_000, 5)
    assert item.calculate_total_price() == 100_000

def test_calculate_total_price_with_discount():
    item = Item("Приставка", 50_000, 12)
    Item.pay_rate = 0.85
    assert item.calculate_total_price() == 510_000

def test_multiple_items():
    item1 = Item("Ноутбук", 20_000, 5)
    item2 = Item("Приставка", 50_000, 12)
    assert len(Item.all) == 2  # Проверяем, что оба экземпляра добавлены в список
    assert item1.calculate_total_price() == 100_000
    assert item2.calculate_total_price() == 600_000

def test_apply_discount():
    item = Item("Телевизор", 30_000, 3)
    Item.pay_rate = 0.9  # Устанавливаем скидку 10%
    item.apply_discount()  # Применяем скидку
    assert item.price == 27_000  # Проверяем, что цена уменьшилась на 10%


if __name__ == "__main__":
    pytest.main()

