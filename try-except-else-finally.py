a, b = 1, 1

try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
# else statement is run when there is no exception raised in the try block.
else:
    print("no exceptions raised")
# If you need to run something irrespective of exception, use finally.
finally:
    print("Run this always")
