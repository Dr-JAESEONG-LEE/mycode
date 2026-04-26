import time

def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@my_timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

print(f"\nslow_add의 정체: {slow_add}")
print(f"slow_add의 이름: {slow_add.__name__}")

