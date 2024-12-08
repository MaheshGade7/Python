import threading
import time

# Shared counter variable
counter = 0
# Create a Lock for synchronization
lock = threading.Lock()

# Thread function
def thread_function(name):
    global counter
    for i in range(5):
        with lock:  # Lock is acquired here
            counter += 1
            print(f"Thread {name}: counter = {counter}")
        time.sleep(0.1)  # Simulate work by sleeping for 0.1 seconds
    print(f"Thread {name} finished.")

# Create threads
threads = []
for i in range(3):  # Create 3 threads
    thread = threading.Thread(target=thread_function, args=(f"Thread-{i+1}",))
    threads.append(thread)

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
print(f"Final counter value: {counter}")
