def tuition_fee(credits, rate):
    return credits * rate


def late_fee(days_late, daily_rate):
    if days_late <= 0:
        return 0
    return min(days_late * daily_rate, 500)


def apply_scholarship(fee, percent):
    return round(fee - fee * percent / 100, 2)


def installment_plan(total, months):
    base = total // months
    last = total - base * (months - 1)
    return [base] * (months - 1) + [last]


def is_fee_cleared(paid, due):
    return paid >= due
