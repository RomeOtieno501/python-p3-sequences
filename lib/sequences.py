#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < length:
            next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_value)
        print(fibonacci_sequence)

# Example usage:
print_fibonacci(9)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
