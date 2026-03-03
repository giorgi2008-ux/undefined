numbers = [2,5,3,4,5]    
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
print(sum_two_smallest_numbers(numbers))    