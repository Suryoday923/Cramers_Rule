import numpy as np

print("CRAMER'S RULE")
print()

# Equation 1
print("Equation 1")
a1 = float(input("Coefficient of x: "))
b1 = float(input("Coefficient of y: "))
c1 = float(input("Coefficient of z: "))
d1 = float(input("Coefficient of w: "))
e1 = float(input("Constant: "))

# Equation 2
print("\nEquation 2")
a2 = float(input("Coefficient of x: "))
b2 = float(input("Coefficient of y: "))
c2 = float(input("Coefficient of z: "))
d2 = float(input("Coefficient of w: "))
e2 = float(input("Constant: "))

# Equation 3
print("\nEquation 3")
a3 = float(input("Coefficient of x: "))
b3 = float(input("Coefficient of y: "))
c3 = float(input("Coefficient of z: "))
d3 = float(input("Coefficient of w: "))
e3 = float(input("Constant: "))

# Equation 4
print("\nEquation 4")
a4 = float(input("Coefficient of x: "))
b4 = float(input("Coefficient of y: "))
c4 = float(input("Coefficient of z: "))
d4 = float(input("Coefficient of w: "))
e4 = float(input("Constant: "))


A = np.array([
    [a1, b1, c1, d1],
    [a2, b2, c2, d2],
    [a3, b3, c3, d3],
    [a4, b4, c4, d4]
])


B = np.array([e1, e2, e3, e4])

# Calculate D
D = np.linalg.det(A)

# Calculate Dx
X = A.copy()
X[:, 0] = B
Dx = np.linalg.det(X)

# Calculate Dy
Y = A.copy()
Y[:, 1] = B
Dy = np.linalg.det(Y)

# Calculate Dz
Z = A.copy()
Z[:, 2] = B
Dz = np.linalg.det(Z)

# Calculate Dw
W = A.copy()
W[:, 3] = B
Dw = np.linalg.det(W)


print("\nD =", round(D, 2))
print("Dx =", round(Dx, 2))
print("Dy =", round(Dy, 2))
print("Dz =", round(Dz, 2))
print("Dw =", round(Dw, 2))


if D == 0:
    print("\nNo unique solution.")
else:
    x = Dx / D
    y = Dy / D
    z = Dz / D
    w = Dw / D

    print("\nSolution:")
    print("x =", round(x, 2))
    print("y =", round(y, 2))
    print("z =", round(z, 2))
    print("w =", round(w, 2))
