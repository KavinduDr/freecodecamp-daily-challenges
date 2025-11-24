def is_valid_number(n, base):
    if not (2 <= base <= 36):
        return False

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_chars = digits[:base]
    n = n.upper()

    return all(char in valid_chars for char in n)

# Example usage:
print(is_valid_number('ABC', 20))      # True
print(is_valid_number('5G3F8F', 17))   # True