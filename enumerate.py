# The following script uses enumerate to iterate through values in a list along with their indices.

my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    # Two different formats to print
    print('{0}: {1}'.format(index, value))
    print(f"{index}: {value}")

# 0: a
# 1: b
# 2: c
# 3: d
# 4: e