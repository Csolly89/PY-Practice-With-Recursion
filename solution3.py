def fibbonacci(n):
    if n<= 0:
        print("YOU SHALL NOT PASS")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)


print("5th fib number:")
print(fibbonacci(5))

print("4th fib number:")
print(fibbonacci(4))

print("10th fib number:")
print(fibbonacci(10))