cars = ["volvo", "audi", "honda", "toyota", "kia", "opel"]
print(f"{[car.title() for car in cars]}")

car = "ford"
print(f"{car.title()} is in the list: {car in cars}")

car = "audi"
print(f"{car.title()} is in the list: {car in cars}")

car = "fiat"
print(f"{car.title()} is in the list: {cars.__contains__(car)}")

car = "opel"
print(f"{car.title()} is in the list: {cars.__contains__(car)}")
