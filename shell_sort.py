# Algorithm:

# Step 1 − Start
# Step 2 − Initialize the value of gap size. Example: h
# Step 3 − Divide the list into smaller sub-part. Each must have equal intervals to h
# Step 4 − Sort these sub-lists using insertion sort
# Step 5 – Repeat this step 2 until the list is sorted.
# Step 6 – Print a sorted list.
# Step 7 – Stop.

# Pseudocode :

# PROCEDURE SHELL_SORT(ARRAY, N)  
#    WHILE GAP < LENGTH(ARRAY) /3 :
#                     GAP = ( INTERVAL * 3 ) + 1      
#    END WHILE LOOP
#    WHILE GAP > 0 :
#        FOR (OUTER = GAP; OUTER < LENGTH(ARRAY); OUTER++):
#              INSERTION_VALUE = ARRAY[OUTER]
#                     INNER = OUTER;
#              WHILE INNER > GAP-1 AND ARRAY[INNER – GAP] >= INSERTION_VALUE:
#                     ARRAY[INNER] = ARRAY[INNER – GAP]
#                     INNER = INNER – GAP
#               END WHILE LOOP
#                   ARRAY[INNER] = INSERTION_VALUE
#        END FOR LOOP
#        GAP = (GAP -1) /3;    
#    END WHILE LOOP
# END  SHELL_SORT

# Python3 program for implementation of Shell Sort
# Python3 program for implementation of Shell Sort

def shellSort(arr, n):
	# code here
	gap=n//2
	
	
	while gap>0:
		j=gap
		# Check the array in from left to right
		# Till the last possible index of j
		while j<n:
			i=j-gap # This will keep help in maintain gap value
			
			while i>=0:
				# If value on right side is already greater than left side value
				# We don't do swap else we swap
				if arr[i+gap]>arr[i]:

					break
				else:
					arr[i+gap],arr[i]=arr[i],arr[i+gap]

				i=i-gap # To check left side also
							# If the element present is greater than current element
			j+=1
		gap=gap//2





# driver to check the code
arr2 = [12, 34, 54, 2, 3]
print("input array:",arr2)

shellSort(arr2,len(arr2))
print("sorted array",arr2)

# This code is contributed by Illion
