def sum_numbers(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

my_list = [1, 2, 3, 4, 5]
total = sum_numbers(my_list)
print(total)  