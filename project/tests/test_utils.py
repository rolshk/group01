def get_ticket_price(age: int) -> float:
    BASE_PRICE = 100.0

    if age < 6:
        return 0.0
    elif 6 <= age <= 17:
        return BASE_PRICE * 0.5
    elif 18 <= age <= 59:
        return BASE_PRICE
    else:  # 60+
        return BASE_PRICE * 0.7


if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        price = get_ticket_price(age)
        print(f"Ticket price: {price} грн")
    except ValueError:
        print("Incorrect number")

def test_child_free():
    assert get_ticket_price(3) == 0.0


def test_teen_half_price():
    assert get_ticket_price(15) == 50.0


def test_adult_full_price():
    assert get_ticket_price(40) == 100.0


def test_senior_discount():
    assert get_ticket_price(70) == 70.0

#uv run -m pytest -v -s
