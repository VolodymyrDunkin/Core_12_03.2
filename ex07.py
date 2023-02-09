from ex06 import all_sum



def create_string(num):
    return f"This is num - {num}"

# result = all_sum(*[n for n in range(100)])

def main():
    str_result = create_string(all_sum(*[n for n in range(100)]))
    return str_result


if __name__ == "__main__":
    print(main())

