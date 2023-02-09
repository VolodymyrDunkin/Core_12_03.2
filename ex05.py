'''Розбити список на частини'''
from random import randint

lst = [randint(100, 1000) for _ in range(100)]

def get_min_max(lst, avg=50):
    min_num = []
    max_num = []
    for i in lst:
        if i <= avg:
            min_num.append(i)
        else:
            max_num.append(i)
    return min_num, max_num

res1, res2 = get_min_max(lst, 200)
print(len(res1), len(res2))