def manual_min(numbers):
    min_num = numbers[1]

    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

numbers = [14, 454, 465, 564, 654, 34653, 23234, 23523565, 2635643, 34634, 436346454]

print(manual_min(numbers))