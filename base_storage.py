from typing import Dict

from abstact_storage import AbstractStorage
from exeption import NotEnoughSpaceError, UnknownProductError, NotEnoughSpaceProductError


class Storage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, amount: int) -> None:
        """ Увеличивает запас items """
        self._items[name] = self._items.get(name, 0) + amount

    def remove(self, name: str, amount: int) -> None:



        self._items[name] -= amount
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self, amount: int) -> bool:
        volume = self._capacity - sum(self._items.values())
        if volume < amount:
            raise NotEnoughSpaceError
        return True

    def get_items(self) -> dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)

    def checks_product_availability(self, name: str, amount: int) -> None:
        if name not in self._items:
            raise UnknownProductError

        if self._items[name] < amount:
            raise NotEnoughSpaceProductError
