import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Funksiya boshlanish vaqti
        result = func(*args, **kwargs)
        end_time = time.time()  # Funksiya tugash vaqti
        execution_time = end_time - start_time  # Vaqt farqini hisoblash
        print(f"Funksiya ishlash uchun ketgan vaqt: {execution_time:.6f} soniya")
        return result
    return wrapper

@time_decorator
def fibonachi(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]  # Fibonachi ketma-ketligining dastlabki ikki elementi
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]  # Yangi qiymatni hisoblash
        fib_sequence.append(next_value)  # Qiymatni ketma-ketlikka qo'shish
    return fib_sequence


n = 22
result = fibonachi(n)
print("Fibonachi ketma-ketligi:", result)
