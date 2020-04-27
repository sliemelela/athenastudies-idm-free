letters = ["a", "b", "c", "d"]
x = 10
while x < 20:
	if x % 5 == 0:
		for letter in letters:
			print("Hello! " + letter)
	else:
		print("bye!")
	x = x + 1				
