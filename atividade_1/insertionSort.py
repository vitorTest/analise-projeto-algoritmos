import argparse
import time

def insertionSort(A):
	"""
		Sort an array through the Insertion Sort Algorithm
		return algorithm's elapsed time
	"""
	start_time = time.time()

	for j in range(1, len(A)):
		key = A[j]
		i 	= j - 1
		
		while i > -1 and A[i] > key:	
			A[i + 1] = A[i]				
			i = i - 1
		
		A[i + 1] = key

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

	elapsed_time = insertionSort(unsorted_array)		
	
	for number in unsorted_array:
		print(number) 

	print("\nArray sorted in {} seconds".format(elapsed_time))
