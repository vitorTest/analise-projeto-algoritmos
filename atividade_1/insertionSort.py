
B = []

def insertionSort(A):
	"""
		Implementacao "purista" do algoritmo Insertion Sort		
	"""

	for j in range(1, len(A)):
		key = A[j]
		i 	= j - 1
		
		while i > -1 and A[i] > key:	
			A[i + 1] = A[i]				
			i = i - 1
		
		A[i + 1] = key


def main():

	unsorted_n_file = open('num.1000.2.in')
	for line in unsorted_n_file:
		number = int(line.strip('\r\n'))
		B.append(number)

	insertionSort(B)		
	for number in B:
		print(number) 

if __name__ == "__main__":
	main()
