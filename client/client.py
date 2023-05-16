from enum import Enum

import requests

BASE_SERVER_HOST = 'http://localhost:8000'


class MathType(Enum):
    EVEN = 'even'
    ODD = 'odd'


def get_random_odd_or_even_from(math_type: MathType):
    response = requests.get(BASE_SERVER_HOST, params={'math_type': math_type.value})
    if not response.ok:
        raise RuntimeError(f'endpoint not found because {response.text}')

    print(response.text)


if __name__ == '__main__':
    get_random_odd_or_even_from(MathType.ODD)
