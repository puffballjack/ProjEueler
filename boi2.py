def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n = n/i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors
list1 = [1,2,3]

def number_of_divisors(n):
	pfactors_list = prime_factors(n)
	pnumbers = list(set(pfactors_list))
	x = 0
	answer = 1
	while True:
		try:
			temp = pfactors_list.count(pnumbers[x])
			answer = answer * (temp + 1)
			x += 1
		except IndexError:
			break
	return answer

def TNE(n):
	return n * (n + 1) / 2 

y = 1
while number_of_divisors(TNE(y)) < 500:
	y += 1
	
print(y)
print(TNE(y))