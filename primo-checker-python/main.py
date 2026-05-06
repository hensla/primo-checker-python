n = int(input("n = "))
primo = True

for i in range(2, n):
    if n % i == 0:
        primo = False
        break

if primo and n > 1:
    print("é primo")
else:
    print("não é primo")