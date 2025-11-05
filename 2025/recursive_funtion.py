num = int(input())

def sum1(num1):
    if num1 <= 1:
        return 1
    else:
        return num1 + sum1(num1-1)

print(sum1(num))
