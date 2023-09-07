from abc import ABC, abstractmethod

class Buildable(ABC):
    @abstractmethod
    def build():
        pass

    @abstractmethod
    def teardown():
        pass
