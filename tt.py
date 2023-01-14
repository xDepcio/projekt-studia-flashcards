from datetime import datetime
from typing import List


class Price:
    def __init__(self, value_gr):
        if value_gr < 0:
            raise ValueError("Price cannot be negative")
        self.value_gr = value_gr

    def __str__(self) -> str:
        formatted_price = self._format_price()
        return f'{formatted_price}'

    def __add__(self, other: 'Price') -> 'Price':
        return Price(self.value_gr + other.value_gr)

    def __sub__(self, other: 'Price') -> 'Price':
        return Price(self.value_gr - other.value_gr)

    def __mul__(self, multiplier: float) -> 'Price':
        return Price(self.value_gr * multiplier)

    def _split_price(self):
        value_zl = self.value_gr // 100
        value_gr = self.value_gr % 100
        return (value_zl, value_gr)

    def _format_price(self):
        zl, gr = self._split_price()
        return f'{zl}.{gr:02}'

    def __eq__(self, other) -> bool:
        return (self.__class__ == other.__class__ and
                self.value_gr == other.value_gr)


class Item:
    def __init__(self, name: str, price: Price):
        if name == "":
            raise ValueError("Name cannot be empty")
        self._name = name
        self._price = price

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> Price:
        return self._price

    def __eq__(self, other) -> bool:
        return (self.__class__ == other.__class__ and
                self._name == other._name)

    def __str__(self):
        return f"{self._name} {self._price}"


class ReceiptPosition:
    def __init__(self, item: Item, number_of_items: int = 0):
        self._item = item
        self._number_of_items = number_of_items

    def __str__(self) -> str:
        amount = str(self.get_amount())
        return f"{self._item} {amount}"

    def format_with_padding(self, name_length, price_length, amount_length):
        amount = str(self.get_amount())
        price_str = str(self._item.get_price())
        item_formatted = f"{self._item.get_name():<{name_length}} {price_str:>{price_length}}"
        return f"{item_formatted} {amount:>{amount_length}}"

    def get_item(self):
        return self._item

    def get_amount(self):
        return self._number_of_items

    def get_str_parts(self):
        return (self._item.get_name(), str(self._item.get_price()), str(self.get_amount()))

    def get_str_lengths(self):
        return (len(x) for x in self.get_str_parts())

    def get_total_price(self) -> Price:
        amount = self.get_amount()
        total_price = self._item.get_price() * amount
        return total_price

    def __eq__(self, other) -> bool:
        return self._item == other._item


class Receipt:
    def __init__(self, positions: List[ReceiptPosition] = None):
        self._positions = [] if positions is None else positions
        self._date = datetime.today()

    def __str__(self):
        name_length, price_length, amount_length = self._find_representation_lengths()
        line_length = name_length + price_length + amount_length + 2  # spaces
        output = str(self._date) + "\n"
        output += "-" * line_length + "\n"
        output += self._format_item_list(name_length, price_length, amount_length)
        output += "-" * line_length + "\n"
        output += self._format_summary(name_length + price_length + 1)
        return output

    def short_summary(self):
    	return f'{str(self._date)} {self._format_summary(50)}'

    def _find_representation_lengths(self):
        lengths = [x.get_str_lengths() for x in self._positions]
        return (max(x) for x in zip(*lengths))

    def _format_item_list(self, *args):
        output = ""
        for position in self._positions:
            output += position.format_with_padding(*args) + "\n"
        return output

    def _format_summary(self, length):
        total_price = str(self.get_total_price())
        prefix = "Total: "
        return f"{prefix}{total_price}\n"

    def add_position(
        self,
        name: str,
        price_gr: int,
        number_of_items: int = 0
    ):
        item = Item(name, Price(price_gr))
        new_position = ReceiptPosition(item, number_of_items)
        if new_position not in self._positions:
            self._positions.append(new_position)
            return new_position

    def remove_position(self, position):
        self._positions.remove(position)

    def get_total_price(self):
        total = Price(0)
        for position in self._positions:
            total = total + position.get_total_price()
        return total
