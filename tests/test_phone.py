import pytest
from src.item import Item
from src.phone import Phone

def test_phone_initialization():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_phone_number_of_sim_setter():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

def  test_phone_number_of_sim_setter_invalid():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone.number_of_sim = 0
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone.number_of_sim = -1
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone.number_of_sim = "two"

def test_phone_addition_with_item():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("Смартфон", 10_000, 20)
    assert phone + item == 25

def test_phone_addition_with_phone():
    phone1 = Phone("iPhone 11", 40_000, 3, 2)
    phone2 = Phone("iPhone 13", 80_000, 9, 2)
    assert phone1 + phone2 == 12

def test_phone_addition_with_invalid_type():
    phone = Phone("iPhone 14", 120000, 5, 2)
    with pytest.raises(TypeError):
        phone + "invalid type"  # Проверяем, что сложение с неправильным типом вызывает ошибку


def test_phone_repr():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_phone_str():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == "iPhone 14"



if __name__ == "__main__":
    pytest.main()