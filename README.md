## Using matrix_invert.py
File takes in a square (nxn) matrix of any size (>2) and prints the inverse matrix while creating a csv file of the inverse. The first argument corresponds to the input matrix csv and the second augment to the output matrix csv. 

#### Argument Format
	python matrix_invert.py <input_matrix> <output_matrix>

#### Example
	python matrix_invert.py .\input_matrix.csv .\output_matrix.csv
	
> Non invertible matrices will return an error: The matrix can not be inverted.

## Using apply_matrix.py
File takes in a square (nxn) matrix and a nx1 vector of any size (>2) and prints the resultant vector while creating an output vector csv. The first argument corresponds to the input matrix csv, the second to the input vector csv, and the third to the output vector csv.

#### Argument Format
	python apply_matrix.py <input_matrix> <input_vector> <output_vector>

#### Example
	python apply_matrix.py .\output_matrix.csv .\input_vector.csv .\output_vector.csv

## Notes
- Written for python 3.0
- apply_matrix.py only functions for square (nxn) matrices. Other sizes will produce incorrect values.
- Accepts and returns csv files
