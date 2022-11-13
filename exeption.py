class BaseError(Exception):
    massage = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    massage = 'Недостаточно места'


class UnknownProductError(BaseError):
    massage = 'Неизвестный товар'


class NotEnoughSpaceProductError(BaseError):
    massage = 'Недостаточно товара'


class BadRequestError(BaseError):
    massage = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    massage = 'Неизвестный склад'


class TooManyUniqueProductsError(BaseError):
    massage = 'Слишком много разных товаров'
