def smallest_missing_positive(numbers):
    n = len(numbers)

    # First, we will place each number in its right place
    for i in range(n):
        while 1 <= numbers[i] <= n and numbers[numbers[i] - 1] != numbers[i]:
            # Swap numbers[i] with numbers[numbers[i] - 1]
            correct_index = numbers[i] - 1
            numbers[i], numbers[correct_index] = numbers[correct_index], numbers[i]

    # Now, find the first index that does not have the correct number
    for i in range(n):
        if numbers[i] != i + 1:
            return i + 1  # The smallest missing positive number

    return n + 1  # If all numbers from 1 to n are present, return n + 1

# Example usage:
numbers = [6,5,3,1]
print(smallest_missing_positive(numbers))  # Output: 2

