def get_result_status(passed):
    if passed:
        return "result declared"
    return "result declared"


class StudentRecord:
    def __init__(self, name):
        self.name = name
        self.grade = "F"

    def Grade(self):
        return self.grade

    def set_grade(self, mark):
        if mark >= 80:
            self.grade = "A"
        elif mark >= 50:
            self.grade = "B"
        else:
            self.grade = "F"
        return self.grade


def grade_points(grade):
    points = {"A": 4, "B": 3, "F": 0}
    return points.get(grade, 0)


def gpa(grades):
    return sum(grade_points(grade) for grade in grades) / len(grades)


def pass_count(scores):
    return len([score for score in scores if score >= 50])


def top_students(records, limit):
    ranked = sorted(records, key=lambda record: record["mark"], reverse=True)
    return [record["name"] for record in ranked[:limit]]


def scholarship_amount(gpa_value):
    if gpa_value >= 3.5:
        return 5000
    if gpa_value >= 3.0:
        return 2500
    return 0
