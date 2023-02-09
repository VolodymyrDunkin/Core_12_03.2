# x = 10

# def fnc():
#     global x
#     x = x + 2
#     print(x)



def fnc(n):
    if n == 3:
        return 3
    return fnc(n-1) + n

print(fnc(5))


# def fnc(a, **k):
#     sum = 0
#     for k in k.values():
#         sum += k
#     return sum

# result = fnc(10, k=1, b=2, c=3, d=4)

# print(result)