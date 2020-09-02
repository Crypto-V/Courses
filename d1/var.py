def my_var():
    my_list = [42, "42", 42.0, True, [42], {42: 42}, (42,), ()]
    for value in my_list:
        print(f"{value} is of type {type(value)}")


if __name__ == "__main__":
    my_var()
