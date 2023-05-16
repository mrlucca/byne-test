from datetime import datetime

from services.gateway.core.interfaces.user_request_repository import IUserRequestRepository


class MathDiscoveryRequestInput:
    email: str
    number: int


class SaveMathDiscoveryRequestFromUserUseCase:
    __slots__ = 'user_request_repository',

    def __init__(self, user_request_repository: IUserRequestRepository):
        self.user_request_repository = user_request_repository

    async def execute(self, request: MathDiscoveryRequestInput):
        await self.user_request_repository.save(
            email=request.email,
            number=request.number,
            created_at=datetime.utcnow()
        )
