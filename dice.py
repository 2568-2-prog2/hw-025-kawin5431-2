import random

class Dice:
    def __init__(self, probabilities: list):
        if not probabilities:
            raise ValueError("Probabilities list cannot be empty.")
        if abs(sum(probabilities) - 1.0) > 1e-6:
            raise ValueError(f"Probabilities must sum to 1.0, got {sum(probabilities)}")
        if any(p < 0 for p in probabilities):
            raise ValueError("All probabilities must be non-negative.")

        self.probabilities = probabilities
        self.faces = list(range(1, len(probabilities) + 1))

    def roll(self) -> int:
        return random.choices(self.faces, weights=self.probabilities, k=1)[0]

    def roll_many(self, n: int) -> list:
        if n <= 0:
            raise ValueError("Number of rolls must be a positive integer.")
        return random.choices(self.faces, weights=self.probabilities, k=n)

    def __repr__(self):
        return f"Dice(faces={len(self.faces)}, probabilities={self.probabilities})"
