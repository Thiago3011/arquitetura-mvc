from src.controllers.pet_delete_controller import PetdeleteController

def test_delete_pet(mocker):
    mocker_repository = mocker.Mock()
    controller = PetdeleteController(mocker_repository)
    controller.delete("Rex")

    mocker_repository.delete_pets.assert_called_once_with("Rex")