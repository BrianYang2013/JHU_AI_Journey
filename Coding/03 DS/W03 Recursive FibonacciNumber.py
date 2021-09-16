def FibonacciNumber(index):
   if (index == 0):
      return 0
   elif (index == 1):
      return 1
   else:
      return FibonacciNumber(index - 1) + FibonacciNumber(index - 2)

user_val = int(input("Please input the Fibonacchi index: "))
print(FibonacciNumber(user_val))