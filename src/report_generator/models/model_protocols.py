from collections.abc import Iterable
from typing import Protocol


class Repository(Protocol):
    def create(self, new_object):
        """
        Persists a new object in the repository and returns a representation of
        it without joins.

        :param new_object: the object to be persisted

        :return: the persisted object
        """

    def create_many(self, new_objects: Iterable):
        """
        Persists an iterable of new objects in the repository and returns None.

        :param new_objects: the objects to be persisted

        :return: None
        """
