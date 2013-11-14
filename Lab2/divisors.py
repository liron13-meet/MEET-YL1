def divisors():
	n=raw_input("enter a number: ")
	n=int(n)
	for i in xrange(n):
		if int(n)%(i+1)==0:
			print i+1

divisors()
