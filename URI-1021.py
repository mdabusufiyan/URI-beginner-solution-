from math import *
N = float(input())
T = floor(N)
P = N - T
T100 = T50 = T20 = T10 = T5 = T2 = T1 = P50 = P25 = P10 = P5 = P1 = p = 0
if T >= 100:
    T100 = int(T / 100)
    T = T % 100
if T >= 50:
    T50 = int(T / 50)
    T = T % 50
if T >= 20:
    T20 = int(T / 20)
    T = T % 20
if T >= 10:
    T10 = int(T / 10)
    T = T % 10
if T >= 5:
    T5 = int(T / 5)
    T = T % 5
if T >= 2:
    T2 = int(T / 2)
    T = T % 2
if T >= 1:
    T1 = int(T / 1)
print(P)

if P >= .50:
    P50 = int(P / .50)
    P = P % .50
if P >= .25:
    P25 = int(P / .25)
    P = P % .25
if P >= .10:
    P10 = int(P / .10)
    P = P % .10
if P >= .05:
    P5 = int(P / .05)
    P = P % .05
if P >= .01:
    P1 = float(P / .01)
    P = P % .01
else:
    P = int(P / .01)
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % T100)
print("%d nota(s) de R$ 50.00" % T50)
print("%d nota(s) de R$ 20.00" % T20)
print("%d nota(s) de R$ 10.00" % T10)
print("%d nota(s) de R$ 5.00" % T5)
print("%d nota(s) de R$ 2.00" % T2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % T1)
print("%d moeda(s) de R$ 0.50" % P50)
print("%d moeda(s) de R$ 0.25" % P25)
print("%d moeda(s) de R$ 0.10" % P10)
print("%d moeda(s) de R$ 0.05" % P5)
print(P)
print("%d moeda(s) de R$ 0.01" % P1)
