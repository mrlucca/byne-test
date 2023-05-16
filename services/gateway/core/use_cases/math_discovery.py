from enum import Enum
import aiohttp
from pydantic import BaseModel


class MathType(Enum):
    EVEN = 'even'
    ODD = 'odd'


class MathRequestInput(BaseModel):
    math_type: MathType


class MathRequestOutput(BaseModel):
    number: int


class MathDiscoveryUrlNotFound(RuntimeError):
    ...


class MathDiscoveryResponseError(RuntimeError):
    ...


class MathDiscoveryUseCase:
    def __init__(self):
        self.urls = {
            MathType.ODD: 'http://service_1:8000',
            MathType.EVEN: 'http://service_2:8000'
        }

    async def execute(self, input_dto: MathType) -> MathRequestOutput:
        print(input_dto)
        request_url = self.urls.get(input_dto)

        if request_url is None:
            raise MathDiscoveryUrlNotFound(request_url)

        async with aiohttp.ClientSession() as session:
            async with session.get(request_url) as response:
                math_response_content = await response.text()

                if not response.ok:
                    raise MathDiscoveryResponseError(math_response_content)

        return MathRequestOutput(
            number=int(math_response_content)
        )
