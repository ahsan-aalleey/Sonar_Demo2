import unittest

from src import dashboard


class DashboardTests(unittest.TestCase):
    def test_class_report(self):
        self.assertEqual(dashboard.class_report([40, 60, 80]), 60)

    def test_section_report(self):
        self.assertEqual(dashboard.section_report([40, 60, 80]), 60)

    def test_attendance_percent(self):
        self.assertEqual(dashboard.attendance_percent(18, 20), 90)

    def test_late_students(self):
        arrivals = {"Ali": 5, "Sara": 20}
        self.assertEqual(dashboard.late_students(arrivals, 10), ["Sara"])

    def test_grade_distribution(self):
        self.assertEqual(dashboard.grade_distribution(["A", "B", "A"]), {"A": 2, "B": 1})
