import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-W', type=int, dest="capacity")
parser.add_argument('-w', type=int, nargs="+", dest="weights", default=[])
parser.add_argument('-n', type=int, dest="bars_number")

args = parser.parse_args()

capacity = args.capacity
weights = args.weights
bars_number = args.bars_number

if bars_number != len(weights):
	print('Weights count not match with bars number')
else:
	resultSum = 0
	i = 0
	while i < bars_number:
		sum = 0
		if i < (bars_number - 1):
			if weights[i] <= capacity:
				sum = weights[i]
			else:
				continue
			j = i + 1
			while j < bars_number:
				if sum > resultSum:
					resultSum = sum
				sum = weights[i]
				k = j
				while k < bars_number:
					if (sum + weights[k]) <= capacity:
						sum = sum + weights[k]
					k += 1
				j += 1
			if sum > resultSum:
				resultSum = sum

		else:
			if (weights[i] > resultSum) and (weights[i] <= capacity):
				resultSum = weights[i]
		i += 1
	print('Maximum weight of gold: ' + str(resultSum))

