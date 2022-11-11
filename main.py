


class Storage:
    def __init__(self, items: dict, capacity):
        self.items = items
        self.capacity = capacity

    def check_product(self, item: dict):
        """ проверяет наличие товара на складе """
        # Получаем количество товара по названию
        print(item)
        # it = [value for key, value in self.items.items() if key == item.keys()]
        # print(it)
        return item


    def add(self, items):
        """ увеличивает запас items """
        pass

    def remove(self, items):
        """ уменьшает запас items """
        pass

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


class Shop(Storage):
    """
    Реализуйте класс Shop. В нем хранится не больше 5 разных товаров.
    Shop не может быть наполнен, если свободное место закончилось или в нем уже есть 5 разных товаров.
    """
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)


class Recuest:
    """
    Создайте класс Request в котором будет храниться запрос
    Поля:
    from - откуда везем (строка)
    to - куда везем (строка)
    amount = 3,
    product = "печеньки" (строка)

При инициализации  принимает список всех складов и строку типа
    """

def main(massage):
    sms = massage.split()
    # Получаем из запроса количество товара
    number = ''.join([i for i in sms if i.isdigit()])
    # Получаем словарь вида запрошенный товар: количество
    item = {sms[i]:sms[i-1] for i in range(len(sms)) if sms[i-1].isdigit()}
    print(item)
    product.check_product(number)




#print(product.items)
#print(*[f'{value}: {key}' for key, value in product.items.items()], sep='\n')



if __name__ == '__main__':
    print("напишите сколько товара нужно доставить в магазин")
    items = {
        'печеньки': 5,
        'парики': 4,
        'фонарики': 11,
        'хлопушки': 7,
        'петарды': 9,
        'звездочки': 8
    }
    # заполнен склад
    product = Store(items)

    masseage = input()
    main(masseage)


