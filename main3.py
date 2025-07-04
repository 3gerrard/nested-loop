def decimal_to_binary_manual(decimal_num):
    """
    Converts a decimal number to its binary representation using successive division.
    """
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer.")
    if decimal_num < 0:
        return "Cannot convert negative numbers with this method without handling two's complement."
    if decimal_num == 0:
        return "0"

    binary_digits = []
    temp_num = decimal_num
    while temp_num > 0:
        remainder = temp_num % 2
        binary_digits.append(str(remainder))
        temp_num //= 2  # Integer division

    # The binary digits are collected in reverse order, so reverse them
    return "".join(binary_digits[::-1])

# Example usage
decimal_number = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary_manual(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_result}")