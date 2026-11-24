def class_report(marks):
    total = sum(marks)
    count = len(marks)
    average = round(total / count, 2)
    median = sorted(marks)[count // 2]
    passed = len([mark for mark in marks if mark >= 50])
    rate = round(passed / count * 100, 1)
    print("Total marks:", total, "Students:", count, "Average:", average)
    print("Median:", median, "Best mark:", max(marks), "Worst mark:", min(marks))
    print("Spread:", max(marks) - min(marks), "Passed:", passed, "Failed:", count - passed)
    print("Pass rate:", rate)
    return average


def section_report(marks):
    total = sum(marks)
    count = len(marks)
    average = round(total / count, 2)
    median = sorted(marks)[count // 2]
    passed = len([mark for mark in marks if mark >= 50])
    rate = round(passed / count * 100, 1)
    print("Total marks:", total, "Students:", count, "Average:", average)
    print("Median:", median, "Best mark:", max(marks), "Worst mark:", min(marks))
    print("Spread:", max(marks) - min(marks), "Passed:", passed, "Failed:", count - passed)
    print("Pass rate:", rate)
    return average


def attendance_percent(present, total):
    return round(present / total * 100, 1)


def late_students(arrivals, limit):
    return [name for name, minutes in arrivals.items() if minutes > limit]


def grade_distribution(grades):
    counts = {}
    for grade in grades:
        counts[grade] = counts.get(grade, 0) + 1
    return counts
