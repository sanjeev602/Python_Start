a = 3
b = 2

try:
    print('resource opened ')
    print(a/b)

    x = int(input('enter a number:'))

except ZeroDivisionError as error:
    print('error: u can not divide a number by zero-', error)

except ValueError as error:
    print('value error -', error )

except Exception as error:
    print('some form of error-', error )


finally:
    print('closed the resource')

print('bye..')


