cont = 1
num = 2

while (cont < 100):
    normal = False
    for i in range(2, num):
        if (num % i == 0):
            normal = True
            break
    if (not normal):
        cont += 1
        print(num, end=' | ')

    num += 1
