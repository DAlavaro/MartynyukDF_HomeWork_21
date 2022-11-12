class Storage:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity


    def add(self, items):
        """ Увеличивает запас items """
        # Получаем количество запрошенного товара из словаря items
        item = ''.join([i for i in items.keys()])
        count_for_shop = [i for i in items.values()][0]
        # Получаем значение имеющиеся на складе словарь по item
        count_stock = [value for key, value in self.items.items() if key == item][0]
        count_stock += count_for_shop
        self.items[item] = count_stock
        return self.items[item]

    def remove(self, items: dict):
        """ Уменьшает запас items """
        # Получаем количество запрошенного товара из словаря items
        item = ''.join([i for i in items.keys()])
        count_for_shop = [i for i in items.values()][0]
        # Получаем значение имеющиеся на складе словарь по item
        count_stock = [value for key, value in self.items.items() if key == item][0]
        count_stock -= count_for_shop
        self.items[item] = count_stock
        return self.items[item]

    def get_free_space(self):
        """ Возвращает количество свободных мест """

    def get_items(self):
        """ Возвращает содержание склада в словаре """

    def get_unique_items_count(self):
        """ Возвращает количество уникальных товаров """


class Store(Storage):
    """
    Реализуйте класс Store. В нем хранится любое количество любых товаров.
    Store не может быть заполнен если свободное место закончилось
    """
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def check_product(self, item: str, count: int):
        """ Проверяет наличие товара на складе """
        count_storage = [int(value) for key, value in self.items.items() if item == key][0]
        if count_storage >= count:
            print('Нужное количество есть на складе')
            print(f'Курьер забрал {count} {item} со склад')
            print(f'Курьер везет {count} {item} со склад в магазин')
            print(f'Курьер доставил {count} {item} в магазин')

            return {item: count}
        else:
            print('Не хватает на складе, попробуйте заказать меньше')
            message = input("\nСколько еще товара нужно доставить в магазин?\n")
            return main(message)



class Shop(Storage):
    """
    Реализуйте класс Shop. В нем хранится не больше 5 разных товаров.
    Shop не может быть наполнен, если свободное место закончилось или в нем уже есть 5 разных товаров.
    """
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)


class Request:
    """
    Создайте класс Request в котором будет храниться запрос
    Поля:
    from - откуда везем (строка)
    to - куда везем (строка)
    amount = 3,
    product = "печеньки" (строка)

При инициализации принимает список всех складов и строку типа
    """


def main(message):
    sms = message.split()
    # Получаем из запроса количество товара
    count = [int(i) for i in sms if i.isdigit()][0]
    # Получаем словарь вида запрошенный товар: количество
    item = ''.join([sms[i] for i in range(len(sms)) if sms[i-1].isdigit()])
    items = stock.check_product(item, int(count))
    stock.remove(items)
    shop.add(items)
    print('\nВ склад хранится:')
    print(*[f'{i} {j}' for i, j in stock.items.items()], sep='\n')
    print('\nВ магазин хранится:')
    print(*[f'{i} {j}' for i, j in shop.items.items()], sep='\n')
    message = input("\nСколько еще товара нужно доставить в магазин?\n")
    return main(message)


if __name__ == '__main__':
    items_stock = {
        'печеньки': 5,
        'собачки': 4,
        'коробки': 11,
        'хлопушки': 7,
        'петарды': 9,
        'звездочки': 8
    }

    items_shop = {
        'печеньки': 2,
        'собачки': 1,
        'коробки': 2,
        'шарики': 10
    }
    # создаем экземпляр класса склада
    stock = Store(items_stock)
    # создаем экземпляр класса магазин
    shop = Shop(items_shop)
    message = input("Сколько товара нужно доставить в магазин?\n")
    main(message)
