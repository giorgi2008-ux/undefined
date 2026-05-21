def print_even_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)

# მაგალითისთვის შევქმნათ რიცხვების სია
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("ლუწი რიცხვებია:")
print_even_numbers(numbers_list)