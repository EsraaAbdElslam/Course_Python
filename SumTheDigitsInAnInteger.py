number = eval(input("Enter a number between 0 and 1000: "))
n1 = number % 10
number = number // 10
n2 = number % 10
n3 = number //10
print("The sum of the digits is " , n1 + n2 + n3)
