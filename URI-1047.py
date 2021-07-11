startHour, startMin, endHour, endMin = list(map(int, input().split()))

dif = ((endHour * 60) + endMin) - ((startHour * 60) + startMin)
# difference between (end - start) in min

if dif <= 0:
    dif = (dif + (24 * 60))

hour, mint = divmod(dif, 60)
print(f"O JOGO DUROU {hour} HORA(S) E {mint} MINUTO(S)")