import threading
import time

def print_numbers(thread_id):
    for i in range(1, 11):
        print(f"Поток {thread_id}: {i}")
        time.sleep(1)

threads = []
num_threads = 3  

for t_id in range(1, num_threads + 1):
    t = threading.Thread(target=print_numbers, args=(t_id,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Все потоки завершили работу.")