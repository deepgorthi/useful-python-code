import time

start_time = time.time()
# Code to check
a, b = 1,2
c = a + b
# Code to check
end_time = time.time()
time_taken_in_micro = (end_time- start_time)*(10**6)

print(f"Time taken in micro_seconds: {time_taken_in_micro} ms")
