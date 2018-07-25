import argparse
import time 

def selectionSort(A, a_size):
	"""
		Sort an array through the Selection Sort Algorithm
		return algorithm's elapsed time
	"""
	start_time = time.time()

	for i in range(a_size):
		min = i

		for j in range(i+1, a_size):
			
			if A[j] < A[min]:
				min = j

		if A[i] != A[min]:
			aux = A[i]
			A[i] = A[min]
			A[min] = aux	

	return time.time() - start_time

if __name__ == "__main__":

	unsorted_array = []
	
	parser 	= argparse.ArgumentParser(description='Sort an unsorted list of numbers')
	parser.add_argument("--file", "-f", type=str, required=True)
	args 	= parser.parse_args()

	unsorted_n_file = open(args.file)
	for line in unsorted_n_file:
		number = int(line.strip('\r\n'))
		unsorted_array.append(number)

	elapsed_time = selectionSort(unsorted_array, len(unsorted_array))		
	for number in unsorted_array:
		print(number) 
		
	print("\nArray sorted in {} seconds".format(elapsed_time))
