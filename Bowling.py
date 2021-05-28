
class Game:

    def __init__(self):
        self._rolls = []

    def is_spare(self,frameIndex):
        return self.get_frame_score(frameIndex) == 10
         
    def get_frame_score(self, frameIndex):
        first = frameIndex*2
        second = first+1

        return (self._rolls[first] if first < len(self._rolls) else 0) + (self._rolls[second] if second < len(self._rolls) else 0)

    @property
    def score(self) -> int:
        score = 0
        rollIndex = 0
        for frameIndex in range(0,10):
            if self.is_spare(frameIndex):
                bonus_roll = (frameIndex+1)*2
                score += 10 + (self._rolls[bonus_roll] if bonus_roll < len(self._rolls) else 0)
                rollIndex += 2
            else:
                score += self.get_frame_score(frameIndex)
                rollIndex +=2
        return score

    def takedown(self, pins_number: int) -> None:
        self._rolls.append(pins_number)