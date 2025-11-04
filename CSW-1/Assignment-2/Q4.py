# ---- Input Two 2x2 Matrices ----
print("Enter elements of Matrix A (2x2):")
A = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

print("\nEnter elements of Matrix B (2x2):")
B = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

# ---- Matrix Addition ----
Sum = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(A[i][j] + B[i][j])
    Sum.append(row)

# ---- Matrix Multiplication ----
Product = []
for i in range(2):
    row = []
    for j in range(2):
        val = 0
        for k in range(2):
            val += A[i][k] * B[k][j]
        row.append(val)
    Product.append(row)

# ---- Sort rows of Product based on row sum ----
# Compute row sums and sort manually
for i in range(2):
    for j in range(2-i-1):
        if sum(Product[j]) > sum(Product[j+1]):
            Product[j], Product[j+1] = Product[j+1], Product[j]

# ---- Display Matrices ----
print("\nMatrix A:")
for r in A:
    print(r)

print("\nMatrix B:")
for r in B:
    print(r)

print("\nSum (A + B):")
for r in Sum:
    print(r)

print("\nProduct (A × B):")
for r in Product:
    print(r)

print("\nSorted Product Matrix based on row sum:")
for r in Product:
    print(r)
