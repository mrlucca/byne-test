from abc import ABC, abstractmethod


class IAuthRepository(ABC):
    @abstractmethod
    async def create_client(self, email: str):
        ...

    @abstractmethod
    async def client_exists_from_email(self, email: str) -> bool:
        ...

