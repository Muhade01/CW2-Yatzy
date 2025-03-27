import random

class Yatzy:
    def __init__(self):
        # Initialize 5 dice (values 1-6) and their lock status
        self.dice = [0] * 5  # List to store the 5 dice values
        self.locked = [False] * 5  # List to track if each die is locked
        self.roll()  # Roll all dice when the class is instantiated

    def roll(self):
        # Roll all unlocked dice
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def lock_die(self, index):
        # Lock a specific die (0-4)
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        # Unlock a specific die (0-4)
        if 0 <= index < 5:
            self.locked[index] = False

    # Scoring methods for individual numbers
    def ones(self):
        return sum(d for d in self.dice if d == 1)

    def twos(self):
        return sum(d for d in self.dice if d == 2) * 2

    def threes(self):
        return sum(d for d in self.dice if d == 3) * 3

    def fours(self):
        return sum(d for d in self.dice if d == 4) * 4

    def fives(self):
        return sum(d for d in self.dice if d == 5) * 5

    def sixes(self):
        return sum(d for d in self.dice if d == 6) * 6

    # More complex scoring methods
    def one_pair(self):
        # Find pairs and return the highest pair score
        counts = [0] * 7  # Index 0 is unused, 1-6 for dice values
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):  # Check from 6 down to 1
            if counts[i] >= 2:
                return i * 2
        return 0

    def two_pairs(self):
        # Find two different pairs and return their sum
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
        # Find three of the same number and return their sum
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 3:
                return i * 3
        return 0

    def four_alike(self):
        # Find four of the same number and return their sum
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 4:
                return i * 4
        return 0

    def small(self):
        # Check for 1, 2, 3, 4, 5 (small straight) = 15 points
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def large(self):
        # Check for 2, 3, 4, 5, 6 (large straight) = 20 points
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def full_house(self):
        # Check for three of one number and two of another
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
        # Sum of all dice
        return sum(self.dice)

    def yatzy(self):
        # Check if all dice are the same = 50 points
        if all(d == self.dice[0] for d in self.dice):
            return 50
        return 0