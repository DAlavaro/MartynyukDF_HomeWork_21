from typing import Dict

from exeption import TooManyUniqueProductsError
from storage import Storage


class Shop(Storage):
    def __init__(self, items: Dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyUniqueProductsError

        super().add(name, amount)
