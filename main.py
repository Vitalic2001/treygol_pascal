num = int(input())
if num >= 0:
    pas1 = [1]
    print(*pas1)
elif num >= 1:
    pas1 = [1,1]
    print(*pas1)
pas2 = [1, 1]
for j in range(2, num + 1):
    pas1 = []
    for i in range(j + 1):
        if i == 0 or i == j:
            pas1.append(pas2[0])
            continue
        pas1.append(pas2[i]+pas2[i-1])
    print(*pas1)
    pas2 = pas1


