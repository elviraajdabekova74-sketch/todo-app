import unittest
from logic import Task


class TestTask(unittest.TestCase):
    def test_create(self):
        t = Task("Купить хлеб", "2026-11-01")
        self.assertEqual(t.title, "Купить хлеб")
        self.assertFalse(t.done)


if __name__ == "__main__":
    unittest.main()