from typing import Dict

from storage import Storage


class Store(Storage):
    def __init__(self, items: Dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)
