# The syntax is:
# digits[start:stop]  # items start through stop-1
# digits[start:]      # items start through the rest of the array
# digits[:stop]       # items from the beginning through stop-1
# digits[:]           # a copy of the whole array

# There is also the step value, which can be used with any of the above:
# digits[start:stop:step] # start through not past stop, by step


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Full list of items: {digits}\n")


# This code prints a slice of the list. The output retains the structure of the
# list, and includes the first three numbers in the list:
start = 0
stop = 3
sliced_list = digits[start:stop]
print(f"digits[0:3] gets the first three items: {sliced_list}\n")


# You can generate any subset of a list. For example, if you want the second,
# third, and fourth items in a list, you would start the slice at index 1 and
# end it at index 4:
start = 1
stop = 4
sliced_list = digits[start:stop]
print(f"digits[1:4] gets subset of the list: {sliced_list}\n")


stop = 5
sliced_list = digits[:stop] # from the very beginning of the list through stop-1
print(f"digits[:5] starts slice at the beginning of the list: {sliced_list}\n")


start = 2
sliced_list = digits[start:] # from start through the end of the list
print(f"digits[2:] from the third item through the last: {sliced_list}\n")


# The other feature is that start or stop may be a negative number, which means
# it counts from the end of the list instead of the beginning. So:
last_item = -1
sliced_list = digits[last_item] # last item in the list
print(f"digits[-1:] gets the last item of the list: {sliced_list}\n")


n_last_items = -2
sliced_list = digits[n_last_items:] # last two items in the list
print(f"digits[-2:] gets the two last items of the list: {sliced_list}\n")


except_n_last_items = -2
sliced_list = digits[:except_n_last_items] # everything except the last two items
print(f"digits[:-2] gets everything except the last two items: {sliced_list}\n")


start = 0
stop = 7
step = 2
sliced_list = digits[start:stop:step] # start through not past stop, by step
print("digits[0:7:2] gets items from the very beginning through 7th item,\n\t" +
    f"(so item[stop-1], i.e. item[6]) with step 2: {sliced_list}\n")


start = 1
stop = 8
step = 3
sliced_list = digits[start:stop:step] # start through not past stop, by step
print("digits[1:8:3] gets items from the 2nd item (so item[1]) through 8th item,\n\t" + 
    f"(so item[stop-1], i.e. item[7]) with step 3: {sliced_list}\n")


# Similarly, step may be a negative number:

step = -1
sliced_list = digits[::step] # all items in the list, reversed
print(f"digits[::-1] gets all items in the list, reversed: {sliced_list}\n")


start = 1
step = -1
sliced_list = digits[start::step] # the first two items, reversed
print(f"digits[1::-1] gets the first two items, reversed: {sliced_list}\n")


stop = -3
step = -1
sliced_list = digits[:stop:step] # the last two items, reversed
print(f"digits[:-3:-1] gets the last two items, reversed: {sliced_list}\n")


start = -3
step = -1
sliced_list = digits[start::step] # everything except the last two items, reversed
print("digits[-3::-1] gets everything except the two last items, " +
    f"reversed: {sliced_list}\n")

