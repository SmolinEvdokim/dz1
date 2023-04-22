# Задача 2: Найдите сумму цифр трехзначного числа.
num = int(input("vvedite trehznachnoe chislo: "))
if num < 100 or num > 999:
    print("False")
else:
    N1 = num // 100
    N2 = (num // 10) % 10
    N3 = num % 10

    sum = N1 + N2 + N3

    print("Summa", num, "ravna:", sum)