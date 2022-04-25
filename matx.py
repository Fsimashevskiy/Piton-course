

M = int(input())
A = []
for i in range(N):
 A.append([0] * M)
print("Enter the first number: ")
g = int(input())
print("Increase: ")
c = int(input())
for i in range(N):
 for j in range(M):
  A[i][j] = g
g += c

for i in range(len(A)):
 for j in range(len(A[i])):
  print(A[i][j], end=' ')
print()
print("The matrix has " + str(N) + " columns and " + str(M) + " string(-s) \n" )