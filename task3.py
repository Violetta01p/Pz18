import threading
import random

numbers = [random.randint(1, 100) for _ in range(1000)]
results = []

def sum_part(part):
    total = sum(part)
    results.append(total)

# Ділимо список на 4 частини
chunk_size = len(numbers) // 4
parts = [
    numbers[0:chunk_size],
    numbers[chunk_size:chunk_size*2],
    numbers[chunk_size*2:chunk_size*3],
    numbers[chunk_size*3:]
]

threads = []

# Створюємо і запускаємо потоки для кожної частини
for part in parts:
    thread = threading.Thread(target=sum_part, args=(part,))
    threads.append(thread)
    thread.start()

# Чекаємо завершення кожного потоку
for thread in threads:
    thread.join()

# Підсумовуємо всі суми
total_sum = sum(results)
print(f"Загальна сума: {total_sum}")
