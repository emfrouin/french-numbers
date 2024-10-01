from naming_helper import nameNumber

# output list of written words (french)

# Input sample 

# input = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75,81,91, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]

print('\x1b[3;30;43m' + 'Get your numbers translated into their written French Names!'+ '\x1b[0m')
print("Enter a comma-seperated list of integers:")
try:
    input = [int(i) for i in input().split(',')]
except:
    raise Exception('Input not a list of integers')
    

output = []

for i in input:
    if i not in ( '[',']'):
        num = int(i)
        name = nameNumber(num)
        output.append(name)
    

print(output)