Countdown-Arithmetic.py

________TALOFA!_______________________________________________________________

Countdown-Arithmetic.py is a simple program designed to solve a simplified 
"countdown" style problem. The user inputs a series of "component" integers, 
then a single "target" integer. The program then determines if the the target 
value can be reached by combining all the component values using addition and 
multiplication operators.

The program takes two lines of input: one containing and arbitrary number of
component values, and one containing a target value and either "L" or "N" 
designating the operating mode of the problem.

A solution in "L" mode means the equation must be solved left to right ie. for
values [1, 2, 3], 1+2*3 would equal 9.

A solution in "N" mode means the equation must be solved "normally" ie. for values
[1, 2, 3], 1+2*3 would equal 7.

The program uses an unsorted binary tree to stores the results of the equation, so
the memory use is exponential with the length of the input. I have tried to mitigate
this by "pruning" the tree- ie. preventing it from building unnecessary branches.

The pruning methods include:

Prune 1: Is this is the second last layer, will the result of the operation result
in the target? If not, don't make it

Prune 2: Will this result in a value higher than the target? If so: do not continue

Prune 3: If this value couldn't possibly reach the target value, do not continue

Prune 4: If the solution is found, stop adding nodes


________HOW TO EXECUTE_________________________________________________________

Countdown-Arithmetic.py will read input from the terminal, or from a file used 
as an argument in execution. To manually input items via terminal, navigate to 
the folder containing arithmetic.py and use the following command: 

$ python3 countdown-arithmetic.py

Type in a string of number to be calculatated you then press enter/return, then type
in the target value followed by 'L' or 'L' indicating the mode

eg.

$ 1 2 3 4 5
$ 25 L

To input a file, place the file containing dates in the same folder as dates.py,
navigate to the folder, and input the following command, followed by the name of
the file containing your input dates.

$ python3 countdown-arithmetic.py [filename]

________TEST_CASES_____________________________________________________________

I have included a file of test cases with the program called "testfile.txt".
If the program is running correctly, it should produce the following output:

Input list contains illegal items: ['1', 'A', '3']
Input list contains illegal items: ['1.2', 'A', '3']
N 7 1 + 2 * 3
N 9 impossible
N 100 impossible
N 100 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 * 9
N 30342 1 + 5 + 89 + 98 * 62 + 46 + 35 + 78 + 23 * 87 * 12
N 1630 1 + 7 * 3 * 8 * 4 + 7 * 3 * 5 * 6 + 4 + 6 * 3 + 3 + 42 + 4 * 65
N 1630 1 + 7 * 3 + 8 + 4 + 7 + 4 * 3 * 5 + 6 * 4 * 6 * 3 * 3 + 42 * 4 + 65
N 12345 1 + 2 * 3 * 4 + 5 * 6 + 7 * 8 * 9 * 10 + 11 + 12 * 13 + 14 * 15 + 16 + 17 + 18 * 19 * 20
L 7 impossible
L 9 1 + 2 * 3
L 100 impossible
Invalid arguments: ['100', 'L', 'E']
L 55489 1 * 5 + 4 * 78 + 9 + 56 + 3 + 2 + 12 + 456 + 3 + 2 + 45 + 65 + 2 * 1 + 321 + 45 + 9 * 8 * 4 + 65
L 12345 impossible

________AUTHOR________________________________________________________________

Mickey Treadwell

Mickey Treadwell 6321880
