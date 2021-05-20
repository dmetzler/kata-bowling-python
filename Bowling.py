
class Game:

    def __init__(self):
        self._score = 0
    
    @property
    def score(self) -> int:
        return self._score

    def takedown(self, pins_number: int) -> None:
        self._score += pins_number