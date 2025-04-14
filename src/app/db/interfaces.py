from abc import ABC, abstractmethod


class IDatabaseService(ABC):
    @abstractmethod
    def _connect(self):
        """Метод для подключения к базе данных."""
        pass

    @property
    @abstractmethod
    def client(self):
        """Свойство для получения клиента базы данных."""
        pass
