from yatzy import Yatzy

def play_yatzy():
    print("Starting a Yatzy game mock-up...")
    game = Yatzy()
    
    # Roll 1: All dice are rolled on instantiation
    print("\nRoll 1:", game.dice)
    print("Scoring options:")
    print(f"Ones: {game.ones()}")
    print(f"Twos: {game.twos()}")
    print(f"Threes: {game.threes()}")
    print(f"Fours: {game.fours()}")
    print(f"Fives: {game.fives()}")
    print(f"Sixes: {game.sixes()}")
    print(f"One Pair: {game.one_pair()}")
    print(f"Two Pairs: {game.two_pairs()}")
    print(f"Three Alike: {game.three_alike()}")
    print(f"Four Alike: {game.four_alike()}")
    print(f"Small Straight: {game.small()}")
    print(f"Large Straight: {game.large()}")
    print(f"Full House: {game.full_house()}")
    print(f"Chance: {game.chance()}")
    print(f"Yatzy: {game.yatzy()}")

    # Roll 2: Lock some dice and roll again
    game.lock_die(0)  # Lock the first die
    game.lock_die(1)  # Lock the second die
    game.roll()
    print("\nRoll 2 (first two dice locked):", game.dice)
    print("Scoring options:")
    print(f"Ones: {game.ones()}")
    print(f"Twos: {game.twos()}")
    print(f"Threes: {game.threes()}")
    print(f"Fours: {game.fours()}")
    print(f"Fives: {game.fives()}")
    print(f"Sixes: {game.sixes()}")
    print(f"One Pair: {game.one_pair()}")
    print(f"Two Pairs: {game.two_pairs()}")
    print(f"Three Alike: {game.three_alike()}")
    print(f"Four Alike: {game.four_alike()}")
    print(f"Small Straight: {game.small()}")
    print(f"Large Straight: {game.large()}")
    print(f"Full House: {game.full_house()}")
    print(f"Chance: {game.chance()}")
    print(f"Yatzy: {game.yatzy()}")

if __name__ == "__main__":
    play_yatzy()