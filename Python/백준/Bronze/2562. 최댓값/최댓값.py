numbers = []
for _ in range(9):
    numbers.append(int(input()))
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers[0], (numbers.index(sorted_numbers[0]))+1,sep='\n')