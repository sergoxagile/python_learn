def total(initial = 5, *numbers, **keywoards):
    count = initial
    for number in numbers:
        count += number
    for key in keywoards:
        count += keywoards[key]
    return count

print(total(1,3,4,5,6,7,84, a = 10, b = 100))