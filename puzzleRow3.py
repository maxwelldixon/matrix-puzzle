def main():
	
	# list of possible numbers I can use 1-16
	a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

	# total combinations tried by computer
	numCombos = 0

	# number of good, unique combinations
	count = 0

	print "First row combinations:"
	print "Number of combinations tried: ", "  ", "Combinations:"
	# loops that generate all possible combinations of 1-16
	for i in range(0,16):
		for j in range(0,16):
			for k in range(0,16):
				for l in range(0,16):
					numCombos += 1
					# equation in the first row
					if a[i] + b[j] + c[k] + d[l] == 42:
						# eliminating duplicate numbers
						if a[i] != b[j]:
							if a[i] != c[k]:
								if a[i] != d[l]:
									if b[j] != c[k]:
										if b[j] != d[l]:
											if c[k] != d[l]:
												count += 1
												print "        ", numCombos, "                      ", a[i], b[j], c[k], d[l]
	print "Total number of good, unique combinations: ", count

main()

