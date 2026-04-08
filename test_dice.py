import unittest
from dice import Dice

class TestDice(unittest.TestCase):

    def test_roll_returns_valid_face(self):
        dice = Dice([1/6] * 6)
        result = dice.roll()
        self.assertIn(result, [1, 2, 3, 4, 5, 6])

    def test_roll_many_length(self):
        dice = Dice([0.1, 0.2, 0.3, 0.1, 0.2, 0.1])
        results = dice.roll_many(10)
        self.assertEqual(len(results), 10)

    def test_roll_many_valid_faces(self):
        dice = Dice([0.1, 0.2, 0.3, 0.1, 0.2, 0.1])
        results = dice.roll_many(100)
        for r in results:
            self.assertIn(r, [1, 2, 3, 4, 5, 6])

    def test_invalid_probability_sum(self):
        with self.assertRaises(ValueError):
            Dice([0.1, 0.2, 0.3])

    def test_invalid_negative_probability(self):
        with self.assertRaises(ValueError):
            Dice([0.5, -0.1, 0.6])

    def test_invalid_empty_probabilities(self):
        with self.assertRaises(ValueError):
            Dice([])

    def test_invalid_roll_many_zero(self):
        dice = Dice([0.5, 0.5])
        with self.assertRaises(ValueError):
            dice.roll_many(0)

    def test_single_face_dice(self):
        dice = Dice([1.0])
        self.assertEqual(dice.roll(), 1)

    def test_biased_dice_custom_faces(self):
        dice = Dice([0.9, 0.1])
        results = dice.roll_many(1000)
        count_1 = results.count(1)
        self.assertGreater(count_1, 700)

if __name__ == '__main__':
    unittest.main()
