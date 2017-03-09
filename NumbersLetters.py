numbers = ["","one","two","three","four","five", "six", "seven", "eight", "nine"]
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
prefixes = [0, 1, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

total = 0
for i in range(1, 1001):
	n = i
	ndigits = [int(i) for i in str(n)]

	if len(ndigits) == 1:
		numstring = numbers[ndigits[0]]
	elif len(ndigits) == 2 and n < 20:
		numstring = tens[ndigits[1]]
	elif len(ndigits) == 2 and n > 19:
		numstring = prefixes[ndigits[0]] + numbers[ndigits[1]]
	elif len(ndigits) == 3:
		if ndigits[1] == 1:
			addon = tens[ndigits[2]]
		elif ndigits[1] > 1:
			addon = prefixes[ndigits[1]] + numbers[ndigits[2]]
		elif ndigits[1] == 0:
			addon = numbers[ndigits[2]]
		numstring = numbers[ndigits[0]] + "hundredand" + addon
		
		if ndigits[1] == 0 and ndigits[2] == 0:
			numstring = numbers[ndigits[0]] + "hundred"
	elif len(ndigits) == 4:
		numstring = "onethousand"

	total += len(numstring)
	print(numstring)

print(total)
