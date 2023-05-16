from abc import ABC, abstractmethod
from datetime import datetime


class IUserRequestRepository(ABC):

    @abstractmethod
    async def save(self, email: str, number: int, created_at: datetime):
        ...
