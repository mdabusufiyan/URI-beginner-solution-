s = float(input())
if 0 <= s <= 400:
    i = s * 0.15
    b = s + i
    p = 15
    print("Novo salario: %.2f" % b)
    print("Reajuste ganho: %.2f" % i)
    print("Em percentual: {} {}".format(p, "%"))
elif 400 < s <= 800:
    i = s * 0.12
    b = s + i
    p = 12
    print("Novo salario: %.2f" % b)
    print("Reajuste ganho: %.2f" % i)
    print("Em percentual: {} {}".format(p, "%"))
elif 800 < s <= 1200:
    i = s * 0.10
    b = s + i
    p = 10
    print("Novo salario: %.2f" % b)
    print("Reajuste ganho: %.2f" % i)
    print("Em percentual: {} {}".format(p, "%"))
elif 1200 < s <= 2000:
    i = s * 0.07
    b = s + i
    p = 7
    print("Novo salario: %.2f" % b)
    print("Reajuste ganho: %.2f" % i)
    print("Em percentual: {} {}".format(p, "%"))
elif s > 2000:
    i = s * 0.04
    b = s + i
    p = 4
    print("Novo salario: %.2f" % b)
    print("Reajuste ganho: %.2f" % i)
    print("Em percentual: {} {}".format(p, "%"))
