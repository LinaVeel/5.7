import threading
import time


def print_squares():
    for i in range(1, 11):
        print(f"Квадрат {i}: {i**2}")
        time.sleep(0.1)


def print_cubes():
    for i in range(1, 11):
        print(f"Куб {i}: {i**3}")
        time.sleep(0.1)


square_thread = threading.Thread(target=print_squares)
cube_thread = threading.Thread(target=print_cubes)

square_thread.start()
cube_thread.start()

square_thread.join()
cube_thread.join()

print("Вычисления завершены.")
