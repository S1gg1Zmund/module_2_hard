cipher = [3,21]
cipher_hard = " "
for i in range(3, 21):
    cipher_hard = " "
    for j in range(1, i):
        for k in range(j + 1, i):
            if i % (j + k) == 0:
                cipher_hard += str(j) + str(k)
                print(i, "-", cipher_hard)
