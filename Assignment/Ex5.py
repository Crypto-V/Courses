def multi_merge(list_a, str):
    return list_a + str.split() + list(str.replace(" ", ""))


print(multi_merge([1, 2, 3, 4], "Hello i am Vasile"))
