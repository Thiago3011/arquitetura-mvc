from src.models.sqlite.entities.pets import PetsTable
from .pet_list_controller import PetListController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Luke", type="Dog", id=10),
            PetsTable(name="Fumaca", type="Cat", id=12)
        ]

def test_list_pets():
    controller = PetListController(MockPetsRepository())

    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Luke", "id": 10},
                {"name": "Fumaca", "id": 12}
            ]
        }
    }

    assert response == expected_response