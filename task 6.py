from math import sqrt


def is_prime(num: int) -> bool:
    if num == 1:
        return True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


numbers = (1, 15, 28, 17, 19, 69, 58, 23)
for num in numbers:
    print("Простое" if is_prime(num) else "Составное")
