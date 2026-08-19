def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    checksum = sum(
        (10 - index) * (10 if char == "X" else int(char))
        for index, char in enumerate(isbn)
    )

    return checksum % 11 == 0
