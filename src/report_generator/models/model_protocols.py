from collections.abc import Iterable
from typing import Protocol


class Repository(Protocol):
    def create(self, new_object):
        """
        Persists a new object in the repository and returns a representation of
        it without joins.

        :param new_object: the object to be persisted

        :returns: the persisted object
        """

    def create_many(self, new_objects: Iterable):
        """
        Persists an iterable of new objects in the repository and returns None.

        :param new_objects: the objects to be persisted

        :returns: None
        """

    def get(self, id):
        """
        Fetches an object from the repository by its id.

        :param id: the id of the object to be fetched

        :returns: the fetched object
        """

    def get_many(self, limit: int = 10, offset: int = 0):
        """
        Fetches objects from the repository

        :param limit: The limit of objects to fetch
        :type limit: int
        :param offset: The amount of objects to skip
        :type offset: int

        :returns: The fetched objects
        """

    def get_many_by_field(self, field: str, value):
        """
        Fetches objects from the repository by field

        :param field: The field to filter by
        :type field: str
        :param value: The value of the field to filter

        :returns: The fetched objects

        """

    def update(self, id, updated_fields: dict):
        """
        Updates fields of an object by its id

        :param id: The id of the object to fetch
        :param updated_fields: The fields and values to update
        :returns: The updated object

        """

    def delete(self, id):
        """
        Deletes an object from the repository.

        :param id: the id of the object to be deleted

        :returns: None
        """

    def delete_many(self, ids: Iterable):
        """
        Deletes all objects with the ids from the repository. It does not
        raise an error if an id does not exist, just ignores it.

        :param ids: An iterable of ids of the objects to be deleted

        :returns: None
        """
