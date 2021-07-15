from application.ciphers import caesar, neighbour_swap, random_substitution


class BlackBox:
    """Class that encodes a message with a cypher and checks the solution"""

    def __init__(self, name: str = '', solution: str = ''):
        self.name = name
        self.solved = False
        self.solution = solution
        self.encoded = self._cypher(solution)

    def solve(self, entered: str) -> tuple[str, bool]:
        """Returns the result of solving attempt and if it was successful"""
        attempt = self._cypher(entered)
        is_success = self.encoded == attempt
        if is_success:
            self.solved = True
        return attempt, is_success

    def _cypher(self, entered: str) -> str:
        return entered


class CaesarPuzzle(BlackBox):
    """Puzzle that encodes message with caesar cypher"""

    def __init__(self, key: int, name: str = '', solution: str = ''):
        self.key = key
        super().__init__(name, solution)

    def _cypher(self, entered: str) -> str:
        return caesar(entered, self.key)


class NeigbourSwapPuzzle(BlackBox):
    """Puzzle that encodes message with neighbour swap cypher"""

    def _cypher(self, entered: str) -> str:
        return neighbour_swap(entered)


class RandomSubstitutionPuzzle(BlackBox):
    """Puzzle that encodes message with random substitution cypher"""

    def __init__(self, seed: int, name: str = '', solution: str = ''):
        self.seed = seed
        super().__init__(name, solution)

    def _cypher(self, entered: str) -> str:
        return random_substitution(entered, self.seed)
