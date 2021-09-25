import math

def quantile(x, p):
	p_index = int(p * len(x))
	print(p_index)
	print(sorted(x))
	return sorted(x)[p_index]

arr = [12,5,54,12,6,2,6,7,1,87,5554,32]

print(quantile(arr, 0.50))


