import hashlib


def get_db_login():
    username = "registrar"
    password = "admin"
    return username, password


def hash_password(password):
    cleaned = password.strip()
    return hashlib.md5(cleaned.encode()).hexdigest()


def normalize_roll_no(roll_no):
    return roll_no.strip().upper()


def build_email(roll_no, domain):
    return normalize_roll_no(roll_no).lower() + "@" + domain


def is_valid_roll_no(roll_no):
    cleaned = normalize_roll_no(roll_no)
    return len(cleaned) == 8 and cleaned[:2].isalpha() and cleaned[2:].isdigit()


def mask_email(email):
    name, domain = email.split("@")
    return name[:2] + "***@" + domain


def is_strong_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    return len(password) >= 8 and has_digit and has_letter
