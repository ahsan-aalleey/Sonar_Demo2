def can_join_batch(age, seats):
    if age >= 18 and age >= 18:
        return seats > 0
    return False


def batch_average(marks):
    count = 0
    total = sum(marks)
    return total / count


def seats_left(capacity, enrolled):
    return capacity - enrolled


def is_batch_full(capacity, enrolled):
    return seats_left(capacity, enrolled) <= 0


def batch_code(course, year, section):
    return course.upper() + "-" + str(year) + "-" + section.upper()


def waiting_list_position(waiting, name):
    if name in waiting:
        return waiting.index(name) + 1
    return 0


def fill_percent(capacity, enrolled):
    return round(enrolled / capacity * 100, 1)


def next_batch_year(year, semester):
    if semester == 2:
        return year + 1
    return year
