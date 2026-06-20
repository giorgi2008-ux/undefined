def linear_search(elements, target):
    # მივყვებით სიას ინდექსებით
    for index in range(len(elements)):
        # თუ ვიპოვეთ საძიებო ელემენტი, ვაბრუნებთ მის ინდექსს
        if elements[index] == target:
            return index
    # თუ ვერ ვიპოვეთ, ვაბრუნებთ -1-ს
    return -1

# მაგალითი:
numbers = [4, 2, 9, 1, 7, 5]
print(linear_search(numbers, 10))  # დაგვიბრუნებს 4-ს (რადგან 7 არის მე-4 ინდექსზე)