import pytest
from src.keyboard import Keyboard

def test_keyboard_initialization():
    keyboard = Keyboard("Logitech", 100, 5)
    assert keyboard.name == "Logitech"
    assert keyboard.price == 100
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'

def test_keyboard_repr():
    keyboard = Keyboard("Logitech", 100, 5)
    assert repr(keyboard) == "Keyboard('Logitech', 100, 5, 'EN')"

def test_keyboard_str():
    keyboard = Keyboard("Logitech", 100, 5)
    assert str(keyboard) == "Logitech"

def test_change_language_to_russian():
    keyboard = Keyboard("Logitech", 100, 5)
    keyboard.change_lang()
    assert keyboard.language == 'RU'

def test_change_language_back_to_english():
    keyboard = Keyboard("Logitech", 100, 5)
    keyboard.change_lang()  # Сначала меняем на русский
    keyboard.change_lang()  # Меняем обратно на английский
    assert keyboard.language == 'EN'

if __name__ == "__main__":
    pytest.main()
