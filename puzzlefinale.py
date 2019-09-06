""" This program solves the First Day of School Challenge. It involves filling in 16 missing numbers (only use each number once) into 4 row equations and 4 column equations. First this algorithm finds the unique (no duplicate numbers) combinations for each row and places them into arrays named combosR1, combosR2, combosR3, and combosR4. Then it uses loops with decision structures to determine 4x4 matrices that use the numbers 1-16 only once out of the possible combinations for each row. Finally, the last four lines of the final loop structure use the unique matrices to test the equations in columns 0,1,2,3. If there is a match it prints the total number of iterations used to find the answer and the 4x4 matrix.
"""
import sys, time
from datetime import timedelta

def main():

	a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

	combosR1 = []
	combosR2 = []
	combosR3 = []
	combosR4 = []

	solution = []

	start = time.time()

	# loops that generate all possible combinations of 1-16
	[combosR1.append([a[i], b[j], c[k], d[l]]) for i in range(0,16) for j in range(0,16) for k in range(0,16) for l in range(0,16)
		# equation in row 1
		if a[i] + b[j] + c[k] - d[l] == 31
			# eliminating duplicate numbers
			and a[i] != b[j]
			and a[i] != c[k]
			and a[i] != d[l]
			and b[j] != c[k]
			and b[j] != d[l]
			and c[k] != d[l]]

	# loops that generate all possible combinations of 1-16
	[combosR2.append([a[i], b[j], c[k], d[l]]) for i in range(0,16) for j in range(0,16) for k in range(0,16) for l in range(0,16)
		# ensures (a[i] * b[j]) % c[k] remainder is zero.
		if (a[i] * b[j]) % c[k] == 0
			# equation in row 2
			and (a[i] * b[j]) / c[k] - d[l] == -3
			# eliminating duplicate numbers
			and a[i] != b[j]
			and a[i] != c[k]
			and a[i] != d[l]
			and b[j] != c[k]
			and b[j] != d[l]
			and c[k] != d[l]]												

	# loops that generate all possible combinations of 1-16
	[combosR3.append([a[i], b[j], c[k], d[l]]) for i in range(0,16) for j in range(0,16) for k in range(0,16) for l in range(0,16)
		# equation in row 3
		if a[i] + b[j] + c[k] + d[l] == 42
			# eliminating duplicate numbers
			and a[i] != b[j]
			and a[i] != c[k]
			and a[i] != d[l]
			and b[j] != c[k]
			and b[j] != d[l]
			and c[k] != d[l]]		

	# loops that generate all possible combinations of 1-16
	[combosR4.append([a[i], b[j], c[k], d[l]]) for i in range(0,16) for j in range(0,16) for k in range(0,16) for l in range(0,16)
		# ensures (a[i] + b[j]) % c[k] remainder is zero
		if (a[i] + b[j]) % c[k] == 0
			# equation in row 4
			and (a[i] + b[j]) / c[k] + d[l] == 8
			# eliminating duplicate numbers
			and a[i] != b[j]
			and a[i] != c[k]
			and a[i] != d[l]
			and b[j] != c[k]
			and b[j] != d[l]
			and c[k] != d[l]]										

	# finds the unique matrix based on row combos calculated in the preceding loops
	count = 0
	totalCount = 0
	for i in range(0, 654):
		for j in range(0, 226):
			for k in range(0, 1368):
				for l in range(0, 318):
					totalCount += 1
					# eliminates duplicates for R1[i][0] in columns C1 and C2
					if combosR1[i][0] != combosR2[j][0] and combosR1[i][0] != combosR3[k][0] and combosR1[i][0] != combosR4[l][0] and combosR1[i][0] != combosR2[j][1] and combosR1[i][0] != combosR3[k][1] and combosR1[i][0] != combosR4[l][1]:
						# eliminates duplicates for R1[i][0] in columns C3 and C4
						if combosR1[i][0] != combosR2[j][2] and combosR1[i][0] != combosR3[k][2] and combosR1[i][0] != combosR4[l][2] and combosR1[i][0] != combosR2[j][3] and combosR1[i][0] != combosR3[k][3] and combosR1[i][0] != combosR4[l][3]:
							# eliminates duplicates for R1[i][1] in columns C1 and C2   
							if combosR1[i][1] != combosR2[j][0] and combosR1[i][1] != combosR3[k][0] and combosR1[i][1] != combosR4[l][0] and combosR1[i][1] != combosR2[j][1] and combosR1[i][1] != combosR3[k][1] and combosR1[i][1] != combosR4[l][1]:
								# eliminates duplicates for R1[i][1] in columns C3 and C4
								if combosR1[i][1] != combosR2[j][2] and combosR1[i][1] != combosR3[k][2] and combosR1[i][1] != combosR4[l][2] and combosR1[i][1] != combosR2[j][3] and combosR1[i][1] != combosR3[k][3] and combosR1[i][1] != combosR4[l][3]:
									# eliminates duplicates for R1[i][2] in columns C1 and C2
									if combosR1[i][2] != combosR2[j][0] and combosR1[i][2] != combosR3[k][0] and combosR1[i][2] != combosR4[l][0] and combosR1[i][2] != combosR2[j][1] and combosR1[i][2] != combosR3[k][1] and combosR1[i][2] != combosR4[l][1]:
										# eliminates duplicates for R1[i][2] in columns C3 and C4
										if combosR1[i][2] != combosR2[j][2] and combosR1[i][2] != combosR3[k][2] and combosR1[i][2] != combosR4[l][2] and combosR1[i][2] != combosR2[j][3] and combosR1[i][2] != combosR3[k][3] and combosR1[i][2] != combosR4[l][3]:
											# eliminates duplicates for R1[i][3] in columns C1 and C2
											if combosR1[i][3] != combosR2[j][0] and combosR1[i][3] != combosR3[k][0] and combosR1[i][3] != combosR4[l][0] and combosR1[i][3] != combosR2[j][1] and combosR1[i][3] != combosR3[k][1] and combosR1[i][3] != combosR4[l][1]:
												# eliminates duplicates for R1[i][3] in columns C3 and C4
												if combosR1[i][3] != combosR2[j][2] and combosR1[i][3] != combosR3[k][2] and combosR1[i][3] != combosR4[l][2] and combosR1[i][3] != combosR2[j][3] and combosR1[i][3] != combosR3[k][3] and combosR1[i][3] != combosR4[l][3]:
													# eliminates duplicates for R2[j][0] in columns C1, C2, C3, and R3[k][3]
													if combosR2[j][0] != combosR3[k][0] and combosR2[j][0] != combosR4[l][0] and combosR2[j][0] != combosR3[k][1] and combosR2[j][0] != combosR4[l][1] and combosR2[j][0] != combosR3[k][2] and combosR2[j][0] != combosR4[l][2] and combosR2[j][0] != combosR3[k][3]:
														# elimininates duplicates for R2[j][0] in R4[l][3] and R2[j][1] in columns C1, C2, and C3
														if combosR2[j][0] != combosR4[l][3] and combosR2[j][1] != combosR3[k][0] and combosR2[j][1] != combosR4[l][0] and combosR2[j][1] != combosR3[k][1] and combosR2[j][1] != combosR4[l][1] and combosR2[j][1] != combosR3[k][2] and combosR2[j][1] != combosR4[l][2]:
															# eliminates duplicates for R2[j][1] in column C4 and R2[j][2] in columns C1 and C2
															if combosR2[j][1] != combosR3[k][3] and combosR2[j][1] != combosR4[l][3] and combosR2[j][2] != combosR3[k][0] and combosR2[j][2] != combosR4[l][0] and combosR2[j][2] != combosR3[k][1] and combosR2[j][2] != combosR4[l][1]:
																# eliminates duplicates for R2[j][2] in columns C3 and C4 and R2[j][3] in column C1
																if combosR2[j][2] != combosR3[k][2] and combosR2[j][2] != combosR4[l][2] and combosR2[j][2] != combosR3[k][3] and combosR2[j][2] != combosR4[l][3] and combosR2[j][3] != combosR3[k][0] and combosR2[j][3] != combosR4[l][0]:
																	# eliminates duplicates for R2[j][3] in columns C2, C3, and C4
																	if combosR2[j][3] != combosR3[k][1] and combosR2[j][3] != combosR4[l][1] and combosR2[j][3] != combosR3[k][2] and combosR2[j][3] != combosR4[l][2] and combosR2[j][3] != combosR3[k][3] and combosR2[j][3] != combosR4[l][3]:
																		# eliminates duplicates for R3[k][0] in columns C1, C2, C3, C4
																		if combosR3[k][0] != combosR4[l][0] and combosR3[k][0] != combosR4[l][1] and combosR3[k][0] != combosR4[l][2] and combosR3[k][0] != combosR4[l][3]:
																			# eliminates duplicates for R3[k][1] in columns C1, C2, C3, C4
																			if combosR3[k][1] != combosR4[l][0] and combosR3[k][1] != combosR4[l][1] and combosR3[k][1] != combosR4[l][2] and combosR3[k][1] != combosR4[l][3]:
																				# eliminates duplicates for R3[k][2] in columns C1, C2, C3, C4
																				if combosR3[k][2] != combosR4[l][0] and combosR3[k][2] != combosR4[l][1] and combosR3[k][2] != combosR4[l][2] and combosR3[k][2] != combosR4[l][3]:
																					# eliminates duplicates for R3[k][3] in columns C1, C2, C3, C4
																					if combosR3[k][3] != combosR4[l][0] and combosR3[k][3] != combosR4[l][1] and combosR3[k][3] != combosR4[l][2] and combosR3[k][3] != combosR4[l][3]:
																						# finds correct columns
																						if combosR1[i][0] + combosR2[j][0] - combosR3[k][0] + combosR4[l][0] == 5:
																							if combosR1[i][1] + combosR2[j][1] + combosR3[k][1] + combosR4[l][1] == 51:
																								if combosR1[i][2] + combosR2[j][2] + combosR3[k][2] - combosR4[l][2] == 35:
																									if (combosR1[i][3] * combosR2[j][3]) + combosR3[k][3] - combosR4[l][3] == 32:
																										count += 1
																										elapsedTime = str(timedelta(seconds = time.time() - start))
																										solution.append([combosR1[i], combosR2[j], combosR3[k], combosR4[l]])
																										print(f"{count} solution was found in {elapsedTime}")
																										print(f"{totalCount} combinations were tried.")
																										print("The solution: ")
																										print(solution)
																										sys.exit()

if __name__ == "__main__":
	main()			

