import math


# DCT type II, unscaled.
def transform(vector):
	result = []
	factor = math.pi / len(vector)
	for i in range(len(vector)):
		sum = 0.0
		for (j, val) in enumerate(vector):
			sum += val * math.cos((j + 0.5) * i * factor)
		result.append(sum)
	return result


# DCT type III, unscaled.
def inverse_transform(vector):
	result = []
	factor = math.pi / len(vector)
	for i in range(len(vector)):
		sum = vector[0] / 2.0
		for j in range(1, len(vector)):
			sum += vector[j] * math.cos(j * (i + 0.5) * factor)
		result.append(sum)
	return result


x = [255,255,255,255,255,255,255,255,255,255]
 
print(transform(x))
print(inverse_transform(transform(x)))
