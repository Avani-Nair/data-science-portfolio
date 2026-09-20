import numpy

# read a and b from the user
a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))

if 0 <= a <= 9 and 0 <= b <= 9:  # checks if they are non-negative digit
    print("Valid digits!")

    A = numpy.array([[4*a, -1],  # defining matrix A
                [-3, 9*b]])

    B = numpy.array([[2, -1],   # defining matrix B
                 [-1, 4]])

    A_Transpose = A.transpose()   # Finding transpose of A
    B_Inverse = numpy.linalg.inv(B)  # Finding inverse of B

    # Performing calculation
    result = 64 * numpy.dot(B_Inverse, B_Inverse) + 8 * numpy.dot(B_Inverse, A_Transpose) + 8 * numpy.dot(A_Transpose, B_Inverse) + numpy.dot(A_Transpose, A_Transpose)

    print("Result: ", result)  # displaying the result

    A_Inverse = numpy.linalg.inv(A)  # finding inverse of A
    C = (B - A_Inverse) / 2   # using the given formula to define C
    print("Matrix C: ", C)

    M = numpy.array([[1, 0],  # defining matrix M
                     [2*a, -3]])

    M_det = numpy.linalg.det(M)   # finding the determinant of M
    print("Determinant of M is ", M_det)

    M_Inverse = numpy.linalg.inv(M)  # finding the inverse of M
    print("Inverse of M: ", M_Inverse)

# finding eigenvalues and eigenvectors of M
    eigenvalues, eigenvectors = numpy.linalg.eig(M)
    print("Eigenvalues of M: ", eigenvalues)
    print("Eigenvectors of M: ", eigenvectors)

    P = eigenvectors  # assigning the eigenvector
    print("Matrix P is: ", P)
    P_Inverse = numpy.linalg.inv(P)  # finding the inverse of P

    D = numpy.diag(eigenvalues)  # using eigenvalues to create diagonal matrix D
    print("Matrix D is: ", D)

    M_PDP = numpy.dot(numpy.dot(P, D), P_Inverse)  #creating matrix M using PDP^-1
    print("PDP^-1 is: ", M_PDP)

# verifying if both matrix M have equal values
    verify = numpy.all(numpy.round(M, 5) == numpy.round(M_PDP, 5))
    print("Is it verified?", verify)


else:
    print("Please enter non-negative digits.")

