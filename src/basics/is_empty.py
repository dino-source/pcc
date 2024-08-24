def is_empty(lst: list) -> bool:
    return not bool(lst)


cars = []
list_status = "List is empty"
it_contains = "The list contains following items"
print(f"{list_status}: {is_empty(cars)}. {it_contains}: {cars}")

cars = ["Audi", "Kia"]
print(f"{list_status}: {is_empty(cars)}. {it_contains}: {cars}")
