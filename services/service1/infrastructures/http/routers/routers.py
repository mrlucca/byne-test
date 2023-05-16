from fastapi import APIRouter

from services.service1.core.use_cases.even import EvenUseCase

router = APIRouter()


@router.get('/')
async def random_even():
    use_case = EvenUseCase()
    return use_case.execute()
