def print_numbers():
    with open("number.txt") as f:
        file = f.read()

    converted_file_data = file.split(",")
    for line in converted_file_data:
        print(line)


if __name__ == "__main__":
    print_numbers()
