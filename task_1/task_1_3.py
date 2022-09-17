# Алгоритмы. Лекция 4, задание 1.


from memory_profiler import profile, memory_usage
from random import randint


def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


@memory
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


@memory
def func_3(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


if __name__ == '__main__':
    nums = [randint(0, 10000) for i in range(100000)]

    func_2(nums)
    func_3(nums)

# Оптимизация с помощью filter. Экономия памяти 2 MiB.