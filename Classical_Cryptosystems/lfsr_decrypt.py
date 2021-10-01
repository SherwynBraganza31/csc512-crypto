import numpy as np


#################################################
# Get input and remove delimiters
#################################################
seq = input("Enter in sequence: ")
seq = list(seq.split(", "))

count = 0  #stores the # of consecutive singular matrices
length = 0 #stores the length of the recurrence
sol = 0
tol = 3

print(str(len(seq)))

#for i in range(1, int(len(seq)/2)):
#	matrix = np.zeros((i, i), dtype=int)
#	for x in range(0, i):
#		for y in range(0, i):
#			matrix[x][y] = int(seq[x+y]) - int('0')
#	
#	print(str(i) + " " + str(count), end = " ")
#	print(str(int(np.linalg.det(matrix)%2)) + "\n" + "-------------------------------------------------")
#
#	if count == 5 and  int(np.linalg.det(matrix)%2) == 0:
#		length = i - 6
#		break
#	elif int(np.linalg.det(matrix)%2) == 0:
#		count+=1
#	elif int(np.linalg.det(matrix)%2) == 1:
#		count = 0
#

#######################################################
# Formulate Data into a matrix of size len(seq)/2
#######################################################
seqMatrix = np.zeros((int(len(seq)/2),int(len(seq)/2)), dtype=int)
for x in range(0, int(len(seq)/2)):
	for y in range(0, int(len(seq)/2)):
		seqMatrix[x][y] = seq[x+y]

#######################################################
# Calculate determinants of sub-matrices and stop
# when you encounter 3 consecutive 0 determinants
# stop and check if the last non-singular matrix 
# gives a valid solution. If not continue
#######################################################
for i in range(12, int(len(seq)/2)):
	subMatrix = np.zeros((i,i), dtype=int)
	for x in range(0,i):
		for y in range(0,i):
			subMatrix[x][y] = seqMatrix[x][y]

	det = int(np.linalg.det(subMatrix)%2)
	
	print(i, end="")
	print("   ", end="")
	print(det, end="") 
	print("   ", end="")
	print(count, end="")
	print("\n<<<<<<<<<<<<<<<<")	

	if det == 1:
		count = 0
	elif count == tol and det == 0:
		count = 0
		length = i-tol-1

		rhsMatrix = np.zeros((1,i-tol-1), dtype=int)
		for y in range(0,i-tol-1):
			rhsMatrix[0][y] = seqMatrix[i-tol-1][y]

		subMatrix = np.zeros((i-tol-1,i-tol-1), dtype=int)
		for x in range(0,i-tol-1):
			for y in range(0,i-tol-1):
				subMatrix[x][y] = seqMatrix[x][y]
 		
		print (subMatrix)
		
		subMatrix = np.linalg.inv(subMatrix)
		for x in range(0, i-tol-1):
			for y in range(0,i-tol-1):
				subMatrix[x][y] = int(subMatrix[x][y]%2)

		for x in range(0, i-tol-1):
			for y in range(0,i-tol-1):
				subMatrix[x][y] = int(subMatrix[x][y]%2)

		sol = np.matmul(rhsMatrix,subMatrix)
		for x in range(0,i-tol-1):
			sol[0][x] = int(sol[0][x]%2)
		
		print (subMatrix)
		print (rhsMatrix)
		print (sol)
		
#		for a in range (length+1, int(len(seq)))
#			xor = 	
		break
	elif det == 0:
		count+=1
	

#print("The sequence length is " + str(length))

#matrix = np.zeros((length,length), dtype = int)
#for x in range(0, length):
#	for y in range(0, length):
#		matrix[x,y] = int(seq[x+y]) - int ('0')

#print (matrix)

#matrix = np.linalg.inv(matrix)

#matrix_b = np.zeros(length, dtype=int)
#for x in range(length, length+length):
#	matrix_b[x - length] = int(seq[x]) - int('0')

#matrix_b = np.matmul(matrix_b, matrix)

#for x in range(0, len(matrix_b)):
#	matrix_b[x] = int(matrix_b[x])%2

#print ( matrix_b)


			 
