temp = list(map(float,input().split()))
A, B, C = sorted(temp, reverse=True)
A = float(A); B = float(B); C = float(C)

if A >= B + C:
    print("NAO FORMA TRIANGULO")

elif A*A == ((B*B)+(C*C)):
    print("TRIANGULO RETANGULO")

elif A*A > B*B + C*C:
    print("TRIANGULO OBTUSANGULO")
elif A*A < B*B + C*C:
    print("TRIANGULO ACUTANGULO")


if A == B == C:
    print("TRIANGULO EQUILATERO")

elif (A == B) or (B == C) or (C == A):
    print("TRIANGULO ISOSCELES")