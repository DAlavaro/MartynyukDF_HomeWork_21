from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        """ Увеличивает запас items """
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        """ Уменьшает запас items """
        pass

    @abstractmethod
    def get_free_space(self, amount: int) -> bool:
        """ Возвращает количество свободных мест """
        pass

    @abstractmethod
    def get_items(self) -> dict:
        """ Возвращает содержание склада в словаре """
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """ Возвращает количество уникальных товаров """
        pass

    @abstractmethod
    def checks_product_availability(self, name: str, amount: int) -> None:
        """ Проверяет наличие товара """
        pass

