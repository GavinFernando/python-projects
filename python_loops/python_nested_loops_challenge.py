n = int(input())
print("The factors of", n, "are:")
# Write your code below
for i in range(1,n+1):
    if n%i == 0:
        for j in range(1,n+1):
            if i * j == n:
                print(i,j)
        