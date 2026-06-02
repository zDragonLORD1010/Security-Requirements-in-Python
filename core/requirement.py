from abc import ABC, abstractmethod


class Requirement(ABC):
    id = ""
    title = ""
    severity = ""

    @abstractmethod
    def verify(self):
        pass

    @abstractmethod
    def remediate(self):
        pass
