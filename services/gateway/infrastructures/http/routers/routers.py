from enum import Enum

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services.gateway.core.interfaces.auth_repository import IAuthRepository
from services.gateway.core.services.auth import ClientInput, AuthService, ClientAlreadyExists
from services.gateway.core.use_cases.math_discovery import MathDiscoveryUseCase, MathRequestInput, \
    MathDiscoveryUrlNotFound, MathDiscoveryResponseError, MathType

router = APIRouter()


class InMemoryAuthRepository(IAuthRepository):
    def __init__(self):
        self.emails = {}

    async def create_client(self, email: str):
        self.emails[email] = 0

    async def client_exists_from_email(self, email: str) -> bool:
        return self.emails.get(email) is not None


in_memory_auth_repository = InMemoryAuthRepository()


@router.get('/')
async def get_endpoint_1(math_type: MathType):
    use_case = MathDiscoveryUseCase()
    try:
        out = await use_case.execute(math_type)
    except (MathDiscoveryUrlNotFound, MathDiscoveryResponseError) as e:
        return {
            'success': False,
            'msg': str(e)
        }
    else:
        return {
            'success': True,
            **out.dict()
        }


@router.post('/create_user')
async def create_user(create_user_input: ClientInput):
    try:
        await AuthService(in_memory_auth_repository).create_new_client(create_user_input)
    except ClientAlreadyExists as e:
        return JSONResponse(
            status_code=404,
            content={
                'success': False,
                'error': str(e)
            }
        )

    else:
        return {
            
        }