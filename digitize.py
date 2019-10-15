import time

num = 123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456123456

# using map
start_time_1 = time.time()
list_of_digits = list(map(int, str(num)))
end_time_1 = time.time()

time_taken_in_micro_1 = (end_time_1 - start_time_1)*(10**6)

print(f"This is the map value: {map(int, str(num))}")
print(list_of_digits)
print(f"Time taken using map: {time_taken_in_micro_1}")
# [1, 2, 3, 4, 5, 6]

start_time_2 = time.time()
# using list comprehension
list_of_digits = [int(x) for x in str(num)]
end_time_2 = time.time()

time_taken_in_micro_2 = (end_time_2 - start_time_2)*(10**6)

print(list_of_digits)
print(f"Time taken using for loop: {time_taken_in_micro_2}")
# [1, 2, 3, 4, 5, 6]