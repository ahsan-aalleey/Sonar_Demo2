import unittest

from src import batches


class BatchTests(unittest.TestCase):
    def test_can_join_batch(self):
        self.assertTrue(batches.can_join_batch(20, 5))
        self.assertFalse(batches.can_join_batch(20, 0))
        self.assertFalse(batches.can_join_batch(15, 5))

    def test_batch_average(self):
        with self.assertRaises(ZeroDivisionError):
            batches.batch_average([40, 60])

    def test_seats(self):
        self.assertEqual(batches.seats_left(30, 25), 5)
        self.assertFalse(batches.is_batch_full(30, 25))
        self.assertTrue(batches.is_batch_full(30, 30))

    def test_batch_code(self):
        self.assertEqual(batches.batch_code("cs", 2026, "a"), "CS-2026-A")

    def test_waiting_list_position(self):
        self.assertEqual(batches.waiting_list_position(["a", "b"], "b"), 2)
        self.assertEqual(batches.waiting_list_position(["a", "b"], "z"), 0)

    def test_fill_percent(self):
        self.assertEqual(batches.fill_percent(40, 30), 75)

    def test_next_batch_year(self):
        self.assertEqual(batches.next_batch_year(2026, 2), 2027)
        self.assertEqual(batches.next_batch_year(2026, 1), 2026)
