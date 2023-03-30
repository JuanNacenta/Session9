def factorial(num):
    """
    compute num!
    :param num:
    :return: int, th value of num!
    """
    p = 1
    for i in range(1, num+1):
        p *= i
        return p
    # si no pones el rannge, y solo(num), también multiplicara por 0
print(factorial(4))

result = factorial(10)
print(f"10! = {result}")