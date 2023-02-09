from random import randint

def all_sum(*args):
    result = 0
    
    for i in args:
        result += i
    
    return result


if __name__ == "__main__":
    # print(all_sum(*[randint(10, 100) for _ in range(100)]))
    result = all_sum(100, 100, 200, 300, 5000)

    print(result // 5000)