import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_create():

    person_info = {
        "first_name": "Thiago",
        "last_name": "Henrique",
        "age": 24,
        "pet_id": 1
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():

    person_info = {
        "first_name": "Thiago24",
        "last_name": "Henrique",
        "age": 24,
        "pet_id": 1
    }

    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_info)
