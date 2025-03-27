import random

class Yatzy:
    def __init__(self):
        self.dice = [0] * 5
        self.locked = [False] * 5
        self.roll()

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def lock_die(self, index):
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        if 0 <= index < 5:
            self.locked[index] = False

    # Scoring methods for individual numbers
    def ones(self):
        return sum(d for d in self.dice if d == 1)

    def twos(self):
        return sum(d for d in self.dice if d == 2)

    def threes(self):
        return sum(d for d in self.dice if d == 3)

    def fours(self):
        return sum(d for d in self.dice if d == 4)

    def fives(self):
        return sum(d for d in self.dice if d == 5)

    def sixes(self):
        return sum(d for d in self.dice if d == 6)

    # More complex scoring methods
    def one_pair(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 2:
                return i * 2
        return 0

    def two_pairs(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        pairs = []
        for i in range(1, 7):
            if counts[i] >= 2:
                pairs.append(i * 2)
        if len(pairs) >= 2:
            return sum(pairs[:2])
        return 0

    def three_alike(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 3:
                return i * 3
        return 0

    def four_alike(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 4:
                return i * 4
        return 0

    def small(self):
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def large(self):
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def full_house(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        has_three = False
        has_two = False
        for i in range(1, 7):
            if counts[i] == 3:
                has_three = True
            if counts[i] == 2:
                has_two = True
        if has_three and has_two:
            return sum(self.dice)
        return 0

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        if all(d == self.dice[0] for d in self.dice):
            return 50
        return 0