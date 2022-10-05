###
bemenet = input("Kérem a robot parancsait: ")
kimenet = ""

E = 0
D = 0
N = 0
K = 0

for i in bemenet:
    if i == 'E':
        E= E + 1

for i in bemenet:
    if i == 'D':
        D= D + 1

for i in bemenet:
    if i == 'N':
        N= N + 1

for i in bemenet:
    if i == 'K':
        K= K + 1

print("E betűk száma:  ", E)
print("D betűk száma:  ", D)
print("K betűk száma:  ", K)
print("N betűk száma:  ", N)

x = K - N
y = E - D

for i in range(abs(y)):
    if y > 0:
        kimenet += "E"
        y -= 1
    if y < 0:
        kimenet += "D"
        y += 1

for i in range(abs(x)):
    if x > 0:
        kimenet += "K"
        x -= 1
    if x < 0:
        kimenet += "N"
        x += 1

print(kimenet)
