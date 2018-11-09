given_number = 8
# holder = 1
# for x in range(1, given_number + 1):
#     holder = holder * x
# print(holder)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial(8)