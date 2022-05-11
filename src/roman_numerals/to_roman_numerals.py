def to_roman_numerals(decimal_number: int) -> str:

    if not isinstance(decimal_number, int):
        raise ValueError("Provided argument has to be an int!")

    if decimal_number < 0:
        raise ValueError("Provided number needs to be positive!")

    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(decimal_number / ints[i])
        result.append(nums[i] * count)
        decimal_number -= ints[i] * count
    return ''.join(result)
