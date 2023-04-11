def is_empty(lst: list) -> bool:
    return not bool(lst)

cars = []
print(f"List is empty: {is_empty(cars)}. The list contains following items: {cars}")

cars = ["Audi", "Kia"]
print(f"List is empty: {is_empty(cars)}. The list contains following items: {cars}")

