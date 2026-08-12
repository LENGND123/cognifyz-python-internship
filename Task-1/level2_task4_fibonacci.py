# Level 2 - Task 4: Fibonacci Sequence

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Sequence:")

for i in range(n):
    print(a, end=" ")

    a, b = b, a + b