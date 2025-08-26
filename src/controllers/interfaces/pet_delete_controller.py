from abc import ABC, abstractmethod

class PetdeleteControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
