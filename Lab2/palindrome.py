def palindrome():
	pa1=raw_input("put a word: ")
	pa2=pa1[::-1]
	if pa2==pa1:
		print "palindrome:)"
	else:
		print "not palindrome:("
palindrome() 

