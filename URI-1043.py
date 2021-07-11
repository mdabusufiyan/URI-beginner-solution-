a,b,c = list(map(float,input().split()))

if (a + b > c) and (a + c > b) and (b + c > a) :
    Perimeter = a+b+c
    print(f"Perimetro = {Perimeter:.1f}")
    
else :
    print(f"Area = {((a+b)*c) / 2:.1f}")