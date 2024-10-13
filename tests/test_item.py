"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture(autouse=True)
def clear_item_list():
    # Очищаем список всех экземпляров перед каждым тестом
    Item.all.clear()
    Item.pay_rate = 1.0  # Сбрасываем pay_rate перед каждым тестом


def test_item_creation():   # тест проверяет, что объект item создаётся правильно
    item = Item("Смартфон", 10_000, 20)
    assert item.name == "Смартфон"
    assert item.price == 10_000
    assert item.quantity == 20
    assert len(item.all) == 1

def test_item_name_setter():
    item = Item("ДлинноеИмяТовара", 10_000, 20)
    assert item.name == "ДлинноеИмя"  # Проверяем, что имя обрезается до 10 символов


def test_calculate_total_price_without_discount():  # тест проверяет метод `calculate_total_price` без применения скидки
    item = Item("Ноутбук", 20_000, 5)
    assert item.calculate_total_price() == 100_000


def test_calculate_total_price_with_discount():
    item = Item("Приставка", 50_000, 12)
    Item.pay_rate = 0.85
    assert item.calculate_total_price() == 510_000

def test_apply_discount():
    item = Item("Телевизор", 30_000, 3)
    Item.pay_rate = 0.9  # Устанавливаем скидку 10%
    item.apply_discount()  # Применяем скидку
    assert item.price == 27_000  # Проверяем, что цена уменьшилась на 10%

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('10.99') == 10

def test_instantiate_from_csv(mocker):
    mock_open = mocker.patch("builtins.open",
    mocker.mock_open(read_data="name,price,quantity\nСмартфон,10000,5\nНоутбук,20000,3"))
    Item.instantiate_from_csv("fake_path.csv")

    assert len(Item.all) == 2
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 10000
    assert Item.all[0].quantity == 5
    assert Item.all[1].name == "Ноутбук"
    assert Item.all[1].price == 20000
    assert Item.all[1].quantity == 3

if __name__ == "__main__":
    pytest.main()
