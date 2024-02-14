number = 123456789

digit_sum = lambda x: sum(int(digits) for digits in str(number))
print(digit_sum(number))
