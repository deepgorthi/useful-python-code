############################################################

even = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        even.append("Y")
    else:
        even.append("N")

print(even)
# ['N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']

even = ["Y" if number % 2 == 0 else "N" for number in numbers:]
print(even)
# ['N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y', 'N', 'Y']

############################################################

new_list =[]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 10 == 0:
        new_list.append("ten")
    elif number % 8 ==0:
        new_list.append("eight")
    elif number % 6 == 0:
        new_list.append("six")
    elif number % 4 == 0:
        new_list.append("four")
    else:
        new_list.append(number)

print(new_list)
# [1, 2, 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']

new_list = ["ten" if number % 10 == 0 else "eight" if number % 8 == 0 else "six" if number % 6 == 0 else "four" if number % 4 == 0 else number for number in numbers]
print(new_list)
# [1, 2, 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']

new_list = [
    "ten" if number % 10 == 0
    else "eight" if number % 8 == 0
    else "six" if number % 6 == 0
    else "four" if number % 4 == 0
    else number
    for number in numbers
]
print(new_list)
# [1, 2, 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']

############################################################

############################################################

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)
        
print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


flattened = [item for row in matrix for item in row] 
print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

############################################################

matrix = [[item for item in range(5)] for row in range(3)]
print(matrix)
# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

############################################################

## [Ref Link](https://www.mybluelinux.com/python-list-or-any-iterable-comprehension/)
