
class Game:

    def __init__(self):
        self._rolls = []

    def is_spare(self,frameIndex):
        return self.get_frame_score(frameIndex) == 10

    def is_strike(self,rollIndex):
        return self.score_for_roll(rollIndex) == 10

    def get_frame_score(self, frameIndex):
        first = frameIndex*2
        second = first+1
        return self.score_for_roll(first) + self.score_for_roll(second)

    @property
    def score(self) -> int:
        score = 0
        rollIndex = 0
        for frameIndex in range(0,10):
            if self.is_strike(rollIndex):
                score += 10 + self.score_for_roll(rollIndex + 1) + self.score_for_roll(rollIndex + 2)
                rollIndex += 1
            elif self.is_spare(frameIndex):
                bonus_roll = (frameIndex+1)*2
                score += 10 + self.score_for_roll(bonus_roll)
                rollIndex += 2
            else:
                score += self.get_frame_score(frameIndex)
                rollIndex += 2
        return score

    def takedown(self, pins_number: int) -> None:
        self._rolls.append(pins_number)

    def score_for_roll(self, rollIndex):
        if len(self._rolls) > rollIndex:
            return self._rolls[rollIndex]
        else:
            return 0