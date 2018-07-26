numbers_1 = [8, 19, 148, 4]
numbers_2 = [9, 1, 33, 83]
all_numbers = []

for number1 in numbers_1:
   for number2 in numbers_2:
       mult = number1 * number2
       all_numbers.append(number1 * number2)
print(all_numbers)    
