1. Project Overview

A beginner-friendly Python program to solve a system of four linear equations using Cramer’s Rule and NumPy. The program takes the coefficients of the equations as input, calculates the required determinants, finds the values of the unknown variables, and verifies the final solution.

2. Equations Used

The program is tested using the following four equations:


x + y + 2z - w = 4

x + y - z + w = 2

x + 2y + z - w = 9

x + y + z + w = 3

3. Coefficient Matrix

A =

[ 1   1   2  -1 ]

[ 1   1  -1   1 ]

[ 1   2   1  -1 ]

[ 1   1   1   1 ]

4. Constant Matrix

B = [4, 2, 9, 3]

5. How Cramer’s Rule Works

First, calculate D = det(A). Then replace one column of A with the constant matrix B. The resulting determinants are Dx, Dy, Dz and Dw. The unknowns are calculated as:


x = Dx / D

y = Dy / D

z = Dz / D

w = Dw / D


A unique solution exists when D is not equal to zero.

6. Technologies Used

• Python 3

• NumPy

• Git

• GitHub

7. Installation

Make sure Python is installed on your computer. Install NumPy using:


pip install numpy

8. How to Run

Clone the repository:


git clone https://github.com/Suryoday923/Cramers_Rule.git


Go to the project folder:


cd Cramers_Rule


Run the Python program:


python Cramers_Rule.py

9. User Input

The program asks for the coefficients of x, y, z and w, followed by the constant. For example, for x + y + 2z - w = 4, enter:


Coefficient of x: 1

Coefficient of y: 1

Coefficient of z: 2

Coefficient of w: -1

Constant: 4

10. Sample Output

D = 4.0

Dx = -11.0

Dy = 22.0

Dz = 2.0

Dw = -1.0


Solution:

x = -2.75

y = 5.5

z = 0.5

w = -0.25

11. Verification

The program verifies the solution by substituting the calculated values into the original system. The calculated values are [4. 2. 9. 3.] and the original constants are [4. 2. 9. 3.]. Since they match, the solution is verified successfully.

12. Project Structure

Cramers_Rule/

│

├── Cramers_Rule.py

└── README.md

13. Learning Objectives

• Represent equations using matrices

• Understand coefficient and constant matrices

• Calculate determinants

• Apply Cramer’s Rule

• Perform matrix operations using NumPy

• Solve simultaneous linear equations using Python

• Verify mathematical results

14. Conclusion

This project demonstrates the implementation of Cramer’s Rule using Python and NumPy. The program takes the equation coefficients as input, calculates the required determinants, finds the values of the unknown variables, and verifies the solution using the original equations.


Final solution:

x = -2.75

y = 5.50

z = 0.50

w = -0.25
