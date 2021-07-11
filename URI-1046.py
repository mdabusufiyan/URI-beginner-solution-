x, y = list(map(int, input().split()))
z = 24
if x < y:
    sub = y-x
else:
    sub = (y+z) - x
print(f"O JOGO DUROU {sub} HORA(S)")
