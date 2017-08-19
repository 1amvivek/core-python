def division(dividend, divisor):
    quotient = 0
    while (dividend >= divisor):
        quotient = quotient + 1
        dividend = dividend - divisor

    print("Remainder", dividend)
    return quotient


print("Quotient", division(int(input("Enter dividend")),int(input("Enter Divisor"))))