from pydantic import BaseModel

from services.gateway.core.interfaces.auth_repository import IAuthRepository


class ClientInput(BaseModel):
    email: str


class ClientAlreadyExists(RuntimeError):
    pass


class AuthService:
    def __init__(self, auth_repository: IAuthRepository):
        self.auth_repository = auth_repository

    async def create_new_client(self, client: ClientInput):
        if await self.auth_repository.client_exists_from_email(client.email):
            raise ClientAlreadyExists()

        await self.auth_repository.create_client(client.email)

    async def client_exists(self, email: str) -> bool:
        return await self.auth_repository.client_exists_from_email(email)
