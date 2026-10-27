import importlib
import os
import unittest

# Run against the buggy module with:  GRADEBOOK=buggy_gradebook python -m unittest ...
gb = importlib.import_module(os.environ.get("GRADEBOOK", "gradebook"))


class TestAverage(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(gb.average([50, 100]), 75)

    def test_empty_list_returns_zero(self):
        self.assertEqual(gb.average([]), 0.0)


class TestAddMark(unittest.TestCase):
    def test_calls_do_not_share_state(self):
        gb.add_mark(10)
        self.assertEqual(gb.add_mark(20), [20])

    def test_uses_given_list(self):
        self.assertEqual(gb.add_mark(5, [1, 2]), [1, 2, 5])


class TestLetterGrade(unittest.TestCase):
    def test_boundaries_are_inclusive(self):
        self.assertEqual(gb.letter_grade(90), "A")
        self.assertEqual(gb.letter_grade(75), "B")
        self.assertEqual(gb.letter_grade(50), "C")

    def test_below_and_above(self):
        self.assertEqual(gb.letter_grade(49), "F")
        self.assertEqual(gb.letter_grade(100), "A")


class TestHighest(unittest.TestCase):
    def test_max_in_last_position(self):
        self.assertEqual(gb.highest([10, 20, 99]), 99)

    def test_single_element(self):
        self.assertEqual(gb.highest([7]), 7)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            gb.highest([])


class TestRemoveFailing(unittest.TestCase):
    def test_consecutive_failing_marks(self):
        self.assertEqual(gb.remove_failing([30, 20, 60, 10, 80]), [60, 80])

    def test_input_not_modified(self):
        data = [30, 60]
        gb.remove_failing(data)
        self.assertEqual(data, [30, 60])

    def test_pass_mark_is_inclusive(self):
        self.assertEqual(gb.remove_failing([40, 39]), [40])


if __name__ == "__main__":
    unittest.main()
