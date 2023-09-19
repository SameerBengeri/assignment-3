def reverse_string(input_string):
    reversed_str = ''
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str
original_string = '1234abcd'
reversed_string = reverse_string(original_string)
print(reversed_string)