# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
for i in range(rows):
    line = ""
# Inner loop for columns
    for x in range(cols):
        line += "*"
    print(line)
