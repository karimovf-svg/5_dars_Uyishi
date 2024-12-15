import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Funksiya boshlanish vaqti
        print(f"Funksiya chaqrildi: {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()  # Funksiya tugash vaqti
        execution_time = end_time - start_time  # Vaqt farqini hisoblash
        print(f"Natija: {result}")
        print(f"Funksiya ishlash uchun ketgan vaqt: {execution_time:.6f} soniya")
        return result
    return wrapper

@log_decorator
def DATA(a):
    return sum(a)

DATA([1, 2, 3, 4, 5])
