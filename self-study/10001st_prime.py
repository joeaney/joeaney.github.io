'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def Factorizationer(value):
    subMultiples = []
    tValue = value
    i = 1
    # print('i: %s' % i)
    while i < tValue:
        i += 1
        # print('i: %s \t tValue: %s' % (i, tValue))
        if tValue % i == 0:
            tValue = int(tValue / i)
            # print('gottcha! %s' % i)
            subMultiples.append(i)
            i = 1
            continue
        else:
            continue
    return subMultiples

i = 2
sq = 1
while True:
	factors = Factorizationer(i)
	if len(factors) == 1:
		print(i, sq, factors)
		sq += 1
	elif sq == 10002:
		break
	i += 1
