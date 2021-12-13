# Find Missing And Repeating

# Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

import numpy as np

data = [ 2 , 2 ]

unique = np.array ( data )
mode_count = 0
mode = -1

for index in range ( 0 , len ( unique ) ) :
    temp = data.count ( unique [ index ] )
    if temp > mode_count :
        mode_count = temp
        mode = unique [ index ]
    
if mode > 1 :
    print ( "Repeating Element =" , mode )

n = len ( data )
expected_sum = n * ( n + 1 ) / 2
actual_sum = sum ( data )

sum_diff = int ( expected_sum - actual_sum )

if sum_diff > 0 :
    print ( "Missing Element =" , mode - sum_diff )
    
elif sum_diff < 0 :
    print ( "Missing Element =" ,  mode + sum_diff)
    
else :
    print ( " array has no repeating or missing elements " )
