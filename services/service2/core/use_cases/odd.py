import random


class OddUseCase:
    def execute(self):
        while True:
            n = random.randint(1, 100)

            if n % 2 != 0:
                return n


