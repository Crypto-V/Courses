"""
Define a function called key_list_items that can accept an unlimited number of lists along with another argument
The function should return the second to last item in the specific list specified by the user of the function.

 Example:
     This should return George
     key_list_items("people", objects=['car', 'phone'], people=['Vasile', 'Mike', 'George', 'Peter'])
"""


def key_list_items(key, **kwargs):
    value_list = kwargs[key]
    return value_list[-2]


result = key_list_items("objects", objects=['car', 'phone'], people=['Vasile', 'Mike', 'George', 'Peter'])

print(result)
