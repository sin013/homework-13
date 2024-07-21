n = int(input("введите чисо от 3 - 20"))
result = []
numbers_ = []
Code = True
for i in range(1, n + 1):
    if n % i == 0:
        numbers_.append(i)
print(numbers_)
for i in numbers_:
    for j in range(1, (i // 2)+1):
        k = i - j
        if k + j == i:
            Code = True
        if k == j:
            continue
        if Code == True:
            result.append(j)
            result.append(k)
print(result)
