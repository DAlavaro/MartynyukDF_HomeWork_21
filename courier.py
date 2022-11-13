from typing import Dict
from abstact_storage import AbstractStorage
from request import Request


class Courier:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        # Экземпляр класса Request
        self.__request = request


        self.__from: AbstractStorage = storages[self.__request.out]
        self.__to: AbstractStorage = storages[self.__request.goto]

    def move(self):
        # Проверяет наличие товара на сладе
        self.__from.checks_product_availability(name=self.__request.product, amount=self.__request.amount)
        print(f'{self.__request.amount} {self.__request.product} готово к отправке')

        # Проверяет наличие свободного места при приеме товара
        self.__to.get_free_space(amount=self.__request.amount)

        self.__from.remove(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.out}')
        print(f'Курьер везет {self.__request.amount} {self.__request.product}')

        self.__to.add(name=self.__request.product, amount=self.__request.amount)
        print(f'Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.goto}')
