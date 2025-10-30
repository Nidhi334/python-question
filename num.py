# numbers = [10, 5, 20, 8, 15]

# largest = first = float('inf')
# for num in numbers:
#     if num < largest:
#         first = largest
#         largest = num
#     elif num < first and num != largest:
#         first = num

# print("Second largest number is:", first)


numbers = [10, 900, 200, 1000, 15]

numbers.remove(max(numbers))  # remove the largest
second_largest = max(numbers)
print("Second largest number is:", second_largest)

