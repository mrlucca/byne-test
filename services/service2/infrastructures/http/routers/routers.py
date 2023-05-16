from fastapi import APIRouter

from services.service2.core.use_cases.odd import OddUseCase

router = APIRouter()


@router.get('/')
async def random_odd():
    use_case = OddUseCase()
    return use_case.execute()
