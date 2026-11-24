import unittest

from src import marks


class MarksTests(unittest.TestCase):
    def test_get_result_status(self):
        self.assertEqual(marks.get_result_status(True), "result declared")
        self.assertEqual(marks.get_result_status(False), "result declared")

    def test_student_record(self):
        record = marks.StudentRecord("Sara")
        self.assertEqual(record.Grade(), "F")
        self.assertEqual(record.set_grade(90), "A")
        self.assertEqual(record.set_grade(60), "B")
        self.assertEqual(record.set_grade(10), "F")

    def test_grade_points_and_gpa(self):
        self.assertEqual(marks.grade_points("A"), 4)
        self.assertEqual(marks.grade_points("Z"), 0)
        self.assertEqual(marks.gpa(["A", "B"]), 3.5)

    def test_pass_count(self):
        self.assertEqual(marks.pass_count([40, 50, 90]), 2)

    def test_top_students(self):
        records = [
            {"name": "Ali", "mark": 70},
            {"name": "Sara", "mark": 90},
            {"name": "Omar", "mark": 80},
        ]
        self.assertEqual(marks.top_students(records, 2), ["Sara", "Omar"])

    def test_scholarship_amount(self):
        self.assertEqual(marks.scholarship_amount(3.8), 5000)
        self.assertEqual(marks.scholarship_amount(3.2), 2500)
        self.assertEqual(marks.scholarship_amount(2.0), 0)
