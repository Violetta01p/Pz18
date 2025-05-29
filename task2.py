import threading
import time
import random

def download_file(file_number):
    duration = random.randint(3, 5)
    print(f"Завантаження файлу {file_number}...")
    time.sleep(duration)
    print(f"Файл {file_number} завантажено за {duration} сек.")

threads = []

# Створення і запуск 3 потоків
for i in range(1, 4):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

# Очікуємо завершення всіх потоків
for thread in threads:
    thread.join()

print("Усі файли завантажено.")
