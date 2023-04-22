
S = int(input("vvedite chislo Guravlei(S) "))

if S % 6 != 0:
    print("False")
else:
    p = s = S // 6  
    k = 2 * (p + s)  
    print("P: ", p)
    print("S: ", s)
    print("K: ", k)