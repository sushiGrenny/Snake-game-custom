row = int(input())
for i in range( row, -1, -1):
    for j in range(row, i,-1):
        print(j, end= " ")
    print()
