import time

start_time = time.time()

input("Press Enter to stop the stopwatch...")

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")