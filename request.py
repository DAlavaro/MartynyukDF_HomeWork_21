from typing import Dict

from abstact_storage import AbstractStorage
from exeption import BadRequestError, UnknownStorageError


class Request:

    def __init__(self, request_str: str, storages: Dict[str, AbstractStorage]):
        split_request = request_str.lower().split()
        if len(split_request) != 7 or not split_request[1].isdigit():
            raise BadRequestError

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.out = split_request[4]
        self.goto = split_request[6]

        if self.out not in storages or self.goto not in storages:
            raise UnknownStorageError
