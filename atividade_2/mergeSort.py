#!/usr/bin/env python3

import argparse
import time
from math import floor

def mergeSort(V, beginning, end):
	"""
		Sort an array through the Merge Sort Algorithm.
		return algorithm's elapsed time.		
		Recursively, calls itself, then merge.
	"""
	start_time = time.time()
	# print('mergeSort: ', beginning, end)
	if(beginning < end):
		middle = (beginning + end) // 2
		mergeSort(V, beginning, middle)
		mergeSort(V, middle+1, end)
		merge(V, beginning, middle, end)

	
	for number in V:
		print(number)   	

	return time.time() - start_time

def merge(A, beginning, middle, end):
	"""
		Here is where the algorithm compares, sort and merge the list
	"""
	array1_n_over = True
	array2_n_over = True
	size = end - beginning + 1
	temp = []
	id_array1 = beginning
	id_array2 = middle + 1
	# print('merge: ',beginning, middle, end, size, id_array1, id_array2)

	for id_temp in range(size):

		if array1_n_over and array2_n_over:

			if A[id_array1] <  A[id_array2]:
				temp.append(A[id_array1])
				id_array1 = id_array1 + 1
			else:
				temp.append(A[id_array2])
				id_array2 = id_array2 + 1

			if id_array1 > middle:

				array1_n_over = False

			if id_array2 > end:

				array2_n_over = False

		else:
			if array1_n_over:
				temp.append(A[id_array1])
			else:
				temp.append(A[id_array2])	

	for element in temp:
		A[element] = temp[element]

	# for number in temp:
	# 	print(number)   

if __name__ == "__main__":

	
	unsorted_array = []
	size = 0

	parser 	= argparse.ArgumentParser(description='Sort an unsorted list of numbers')
	parser.add_argument("--file", "-f", type=str, required=True)
	args 	= parser.parse_args()

	unsorted_n_file = open(args.file)
	for line in unsorted_n_file:
		number = int(line.strip('\r\n'))
		unsorted_array.append(number)
		size = size + 1

	elapsed_time = mergeSort(unsorted_array, 0, (size - 1))		
	
	# for number in unsorted_array:
		# print(number) 

	print("\nArray sorted in {} seconds".format(elapsed_time))
