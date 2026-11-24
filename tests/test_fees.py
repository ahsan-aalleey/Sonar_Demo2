import unittest

from src import fees


class FeeTests(unittest.TestCase):
    def test_tuition_fee(self):
        self.assertEqual(fees.tuition_fee(15, 100), 1500)

    def test_late_fee(self):
        self.assertEqual(fees.late_fee(0, 20), 0)
        self.assertEqual(fees.late_fee(5, 20), 100)
        self.assertEqual(fees.late_fee(50, 20), 500)

    def test_apply_scholarship(self):
        self.assertEqual(fees.apply_scholarship(1000, 25), 750)

    def test_installment_plan(self):
        self.assertEqual(fees.installment_plan(1000, 3), [333, 333, 334])

    def test_is_fee_cleared(self):
        self.assertTrue(fees.is_fee_cleared(100, 100))
        self.assertFalse(fees.is_fee_cleared(50, 100))
