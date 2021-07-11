A,B,C = list(map(int,input().split()))
maxAB = ((A+B)+abs(A-B))*.5;
max = ((maxAB+C)+abs(maxAB-C))*.5;
print('%d eh o maior' %max)