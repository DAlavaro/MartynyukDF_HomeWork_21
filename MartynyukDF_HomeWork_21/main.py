


class Storage:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

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


if __name__ == '__main__':
    print_hi('PyCharm')


