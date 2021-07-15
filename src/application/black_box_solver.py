import random

from application.black_box import (
    CaesarPuzzle, NeigbourSwapPuzzle, RandomSubstitutionPuzzle
)


def main() -> None:
    """Runs the puzzles in command line"""
    print("Hello, let's try to solve the black box puzzle")
    print("You'll get an unknown black box, experiment with it to find out how to the get result!")

    words = ["salad", "rickroll", "jam", "python", "help"]

    boxes = [
        CaesarPuzzle(key=7, solution=random.choice(words)),
        NeigbourSwapPuzzle(solution=random.choice(words)),
        RandomSubstitutionPuzzle(seed=3, solution=random.choice(words)),
    ]
    box = random.choice(boxes)
    print(f"You need to enter the string that is transformed to {box.encoded}")
    while not box.solved:
        print("Please, enter your solution")
        print("Enter an empty string to exit")
        entered = input()
        if not entered:
            break
        encoded, is_solved = box.solve(entered)
        print(f'The box outputs "{encoded}"')
        print("Success!" if is_solved else "Try again!")
    print("Farewell!")


if __name__ == '__main__':
    main()
