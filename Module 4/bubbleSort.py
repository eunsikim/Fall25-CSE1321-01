numbers = [3, 5, 2, 7, 1,4,6,10,8,0, 9]
length = len(numbers)

iteration_count = 0
# i is the index
# i is the amount of ordered elements
for i in range(length):
    # At the end of each iteration we can assume
    # the last item in the list is in order
    # hence, we iterate -1 times for each iteration
    # of the outer loop.
    for index in range(length - i - 1):
        iteration_count += 1
        # Check if the current number is higher
        # than the next one, if so swap them
        if numbers[index] > numbers[index + 1]:
            #Swap
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
print(f"Sorted List: {numbers}, and it took me {iteration_count} times") 
