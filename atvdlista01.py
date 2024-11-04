#faça as modificações que se pede 

lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("a lista é: ", lis)
print("o intervalo de 1 á 9 é: ", lis[1:10])
print("o intervalo de 8 á 13 é:", lis[8:14])
print(lis[::2])
print(lis[1::2])
print("multíplos de 2: ", lis[2::2])
print("multíplos de 3: ", lis[3::4])
print("multíplos de 4: ", lis[4::4])

#lista reversa
lis.reverse()
print(lis)

#voltar ao normal
lis.sort()

print(sum(lis[10:16]), "/", sum(lis[3:9])), "ou", sum(lis[10:16])/sum(lis[3:9])