
K = 7
l = (1, 3, 3.5, "a", "zz", 15, 0, 0.5, 0.1, 0.2, "a",)
result = False

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if( (l[i] == l[j]) and (j-i <= K) ):
            result = True
            break

print(result)
