
def get_sum(a, b):
    return a + b

assert (get_sum(1, 2) == 3)
assert (get_sum(2, 2) == 4)
# assert (get_sum(3, 10) == 12) # тут помилка

assert (get_sum(3, 3) == 6)


try:
    a = 1
    b = input()
    print(eval(b))
    if b == '0':
        raise ValueError("Ділити на нуль не можна КАСТОМ")
except (ZeroDivisionError, ValueError) as err:
    if isinstance(err, ValueError):
        print(err)
    else:
        print("Ділити на нуль не можна ДЕФОЛТ")    
except NameError as err:
    print("Такої змінної не існує")
else:
    print("Все гуд")
    pass
finally:
    print("Я завжди виконуюсь")