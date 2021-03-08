#Ways to raise a number to a power:

#can just use multiplication:
print(3 * 3 * 3)

#operator to do it: (returns an int)
print(3 ** 5)

#with the math operator: (returns a double)
import math
result = math.pow(3, 5)
print(result)

#convert math operation to an int:
new_result = math.floor(result)
print(new_result)
