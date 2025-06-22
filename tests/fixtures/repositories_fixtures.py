from collections import UserDict

import pytest


class FakeRepository(UserDict):
    def get(self, id: int):
        return self.data[id]

    def get_all(self, limit: int = 10, offset: int = 0):
        return list(self.data.values())[offset : offset + limit]

    def get_count(self):
        return len(self.data)

    def get_by_field(self, field: str, value):
        for obj in self.data.values():
            if getattr(obj, field) == value:
                return obj

    def update(self, id, updated_object):
        self.data[id] = updated_object

    def create(self, new_object):
        new_object.id = list(self.values())[-1].id + 1 if self.values() else 1
        self.data[new_object.id] = new_object
        return new_object

    def create_many(self, new_objects):
        for new_object in new_objects:
            self.create(new_object)

    def delete(self, id):
        del self.data[id]


@pytest.fixture
def fake_repository() -> type[FakeRepository]:
    return FakeRepository
