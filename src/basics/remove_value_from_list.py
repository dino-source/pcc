motorcycles = ["Yamaha", "Suzuki", "Honda", "Ducati", "Harley Davidson", "Indian"]
print(f"Full list of motorcycles: {motorcycles}")

del motorcycles[1] # delete by index: delete "Suzuki"
print(f"After deleting Suzuki: {motorcycles}")

motorcycles.remove("Ducati") # remove by name: remove "Ducati"
print(f"After removing Ducati: {motorcycles}")

first_owned = motorcycles.pop() # pop the last one and store popped value to variable
print(f"After popping out Indian: {motorcycles}")
print(f"The first motorcycle I owned was a {first_owned}.")

last_owned = motorcycles.pop(1) # pop by index and store popped value to variable
print(f"After popping out Honda: {motorcycles}")
print(f"The last motorcycle I owned was a {last_owned}.")

