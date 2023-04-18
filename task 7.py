def fib(indx: int) -> int:
    if indx == 1 or indx == 2:
        return 1
    return fib(indx - 1) + fib(indx - 2)


for i in range(1, 15):
    print(fib(i))
