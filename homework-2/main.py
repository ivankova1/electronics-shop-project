# -*- coding: windows-1251 -*-

from src.item import Item

if __name__ == '__main__':
    item = Item('�������', 10000, 5)

    # ����� ������������ ������ ������ 10 ��������
    item.name = '��������'
    assert item.name == '��������'

    # ����� ������������ ������ ������ 10 ��������
    item.name = '�������������'
    # Exception: ����� ������������ ������ ��������� 10 ��������.

    Item.all = []
    Item.instantiate_from_csv('/items.csv')   #�������� �������� �� ������ �����
    assert len(Item.all) == 5  # � ����� 5 ������� � ������� �� �������
    item1 = Item.all[0]
    assert item1.name == '��������'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
