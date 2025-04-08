# Worksheet 2: Yatzy Game Implementation


This folder contains the implementation of the Yatzy game in Python, along with tests and GitHub Actions for automated testing.

## Steps
1. **Set Up the Repository**:
   - Created a new GitHub repository `CW2-Yatzy` and cloned it into `portfolio/Worksheet2-Yatzy/CW2-Yatzy/`.
   - Initialized the repository with `README.md`, `repository-link.txt`, `yatzy.py`, `test_yatzy.py`, and a `screenshots` folder (kept local via `.gitignore`).

2. **Implemented the Yatzy Class**:
   - Wrote the `Yatzy` class in `yatzy.py` with 5 dice, each individually lockable.
   - Added a `roll()` method to roll all unlocked dice, with all dice rolled on instantiation.
   - Implemented all required scoring methods: `ones()`, `twos()`, `threes()`, `fours()`, `fives()`, `sixes()`, `one_pair()`, `two_pairs()`, `three_alike()`, `four_alike()`, `small()`, `large()`, `full_house()`, `chance()`, and `yatzy()`.

3. **Wrote Tests**:
   - Created unit tests in `test_yatzy.py` for all methods of the `Yatzy` class.
   - Ran the tests locally with `python3 -m unittest test_yatzy.py` to ensure they passed.

4. **Created a Mock-Up Game**:
   - Wrote `yatzy_game.py` to simulate a game with two rolls, showing the dice and scoring options.
   - See `screenshots/roll1-example.png` for the first roll.
   - See `screenshots/roll2-example.png` for the second roll (with the first two dice locked).

5. **Set Up GitHub Actions**:
   - Added a workflow in `.github/workflows/test.yml` to run tests automatically on push and pull requests.
   - Verified the tests passed in the GitHub Actions tab.
   - See `screenshots/github-actions-example.png` for the successful test run.

Worksheet 3: Using GitHub Issues for Collaboration (Practice Run)

### Steps
1. **Created a Branch**:
   - Made a `collaboration-practice` branch to work on fixes.
2. **Used GitHub Issues**:
   - Classmate (`Classmate01`) created Issue #3: "Bug in `roll()` Method When All Dice Are Locked".
3. **Fixed the Issue**:
   - Updated `roll()` to print a message if all dice are locked.
   - Tested the fix with `yatzy_game.py`.
4. **Merged Changes**:
   - Created a pull request for the `collaboration-practice` branch.
   - Classmate reviewed and approved the PR.
   - Merged the PR into `main` and closed Issue #3.
5. **Main Obstacles and Concerns**:
   - **Obstacles**:
     - Had trouble with Git because I was in the wrong folder (`portfolio` instead of `CW2-Yatzy`).
     - Got indentation errors in `yatzy.py` (like "Unindent amount does not match previous indent").
     - Took time to understand why the `roll()` message was needed.
   - **Concerns**:
     - Need to be careful with Git folders to avoid errors.
     - Should use VS Code to fix indentation automatically.
     - Manual testing works, but automated tests would be better.
## Repository
Link: [CW2-Yatzy](https://github.com/Muhade01/CW2-Yatzy)
