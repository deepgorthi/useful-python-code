dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Values from the second dictionary are used in case of intersections.

# Output
# {'apple': 9, 'banana': 4, 'orange': 8}